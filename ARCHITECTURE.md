# Arquitetura — Controllership Reconciliation Engine

---

## 1. Visão Geral

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            DATA SOURCES                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  ERP CSV    │  │  Bank CSV   │  │  Support    │  │  General Ledger     │ │
│  │  (AR/AP)    │  │  (Multi-bnk)│  │  (PDF/CSV)  │  │  (Razão)            │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
└─────────┼────────────────┼────────────────┼────────────────────┼────────────┘
          └────────────────┴────────────────┴────────────────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │      ETL PIPELINE (Python)       │
                    │  · Parse (csv-parse, pandas)     │
                    │  · Normalize (encoding, decimals)│
                    │  · Validate (schemas, checksums) │
                    │  · Enrich (support matching)     │
                    └───────────────┬────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────────┐
│                      ANALYTICAL ENGINE (Python)                            │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│  │  Aging   │ │   ABC    │ │   Risk   │ │  Top 10  │ │ Turnover │         │
│  │  Bucket  │ │  Pareto  │ │  Matrix  │ │  Accounts│ │  Ratio   │         │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐                      │
│  │ Hierarchy│ │ Temporal │ │ Document │ │ Support  │                      │
│  │  Consolid│ │  Trend   │ │  Types   │ │  Gap     │                      │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘                      │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │      OUTPUT LAYER (JSON/CSV)     │
                    │  Consumido pelo frontend em      │
                    │  tempo de build                  │
                    └───────────────┬────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────────┐
│                         FRONTEND (Angular 17)                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Dashboard AR/AP (17 Seções)                       │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │   │
│  │  │ Executive│ │  Aging   │ │  ABC     │ │  Risk    │ │  Bank    │  │   │
│  │  │  Summary │ │  Chart   │ │  Chart   │ │  Matrix  │ │  Recon   │  │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Filtros de Negócio (Hardcoded Rules)

| Domínio | Regra | Exemplo |
|---|---|---|
| **AR** | Códigos de conta cliente | `1.1.02.01.01.*` |
| **AP** | Prefixo de fornecedores | `2.1.01.01.01` |
| **Aging** | Faixas em dias | 0-30, 31-60, 61-90, 90+ |
| **ABC** | Pareto por valor acumulado | A=80%, B=15%, C=5% |
| **Risco** | Matriz valor × suporte | Alto > R$ 100K sem suporte |

---

## 3. Decisões Arquiteturais (ADRs)

### ADR-001 — ETL em Build-time
**Contexto:** Dados contábeis são volumosos mas relativamente estáticos intra-mês.
**Decisão:** Processar CSVs em tempo de build, gerando JSON estático para o frontend.
**Consequência:** Dashboard carrega instantaneamente; não precisa de backend ativo para leitura.

### ADR-002 — Filtros Hardcoded
**Contexto:** Estrutura contábil do cliente é padronizada (planos de contas fixos).
**Decisão:** Regras de filtro AR/AP hardcoded em Python e TypeScript.
**Consequência:** Performance máxima; desvantagem: requer deploy para mudar regras.

### ADR-003 — Containerização por Banco
**Contexto:** Cada banco tem formato de extrato diferente.
**Decisão:** Container Docker isolado por parser de banco.
**Consequência:** Isolamento de falhas; parsers podem ser versionados independentemente.
