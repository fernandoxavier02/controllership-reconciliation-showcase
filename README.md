# Controllership Reconciliation Engine — Showcase

> **Tipo:** Vitrine técnica arquitetural  
> **Status:** Protótipo público educacional com dados sintéticos
> **Autor:** Fernando Xavier  
> **Domínio:** Conciliação Contábil AR/AP + Conciliação Bancária + Controladoria  
> **Licença:** Proprietário — Todos os direitos reservados. Vitrine para avaliação de portfólio profissional apenas.

---

*Esta vitrine demonstra, em um cenário sintético, como estruturar análises de aging, Pareto, risco, suporte documental e tendências mensais. Não representa um sistema de cliente nem publica resultados de produção.*

---

## 🎯 O Problema de Negócio

Equipes financeiras precisam revisar lançamentos entre:

- **Accounts Receivable (AR)** — clientes, notas fiscais de saída, recebimentos
- **Accounts Payable (AP)** — fornecedores, notas fiscais de entrada, pagamentos
- **Extratos Bancários** — múltiplos bancos com formatos diferentes
- **Saldos do Razão (GL)** — a fonte de verdade contábil

**O gap:** Sem regras explícitas, a identificação de suporte documental, a priorização por valor e a classificação de risco podem depender de planilhas e julgamentos não padronizados.

Resultado: fechamento contábil demorado, auditorias trabalhosas, e decisões de tesouraria baseadas em dados não confiáveis.

---

## 🏗️ A Solução

Protótipo Python que automatiza seis análises sobre lançamentos sintéticos de AR/AP: aging, curva ABC, matriz de risco, contas de maior valor, gaps documentais e tendência mensal.

### Funcionalidades Principais

| Módulo | Descrição | Impacto |
|---|---|---|
| **Suporte Documental** | Identificação de lançamentos sem suporte no fixture | Gaps explícitos |
| **Status de Conciliação** | Resumo de entradas AR/AP e análises calculadas | Revisão reproduzível |
| **Aging de Contas** | Classificação por faixa de atraso (0-30, 31-60, 61-90, 90+) | Priorização de cobrança/pagamento |
| **Top 10 Contas** | Contas de maior valor absoluto (risco concentrado) | Foco no Pareto |
| **Curva ABC** | Classificação por importância (A=80% valor, B=15%, C=5%) | Gestão por exceção |
| **Matriz de Risco** | Classificação Alto/Médio/Baixo por valor e suporte | Regra explícita |
| **Tendência Mensal** | Agrupamento de valores AR/AP por mês | Evolução visível |

---

## 📈 Evidência pública

As imagens abaixo são mockups ilustrativos; a evidência executável está no protótipo Python e nos testes.

### Dashboard AR/AP Executivo
![Dashboard Executivo](assets/screenshots/01-dashboard-executivo.png)

### Aging de Contas
![Aging de Contas](assets/screenshots/02-aging-contas.png)

### Curva ABC
![Curva ABC](assets/screenshots/03-curva-abc.png)

### Matriz de Risco
![Matriz de Risco](assets/screenshots/04-matriz-risco.png)

### Conciliação Bancária
![Conciliação Bancária](assets/screenshots/05-conciliacao-bancaria.png)

### Diagrama de Arquitetura
![Diagrama de Arquitetura](assets/screenshots/06-diagrama-arquitetura.png)

O repositório oferece código executável, seed determinístico, seis análises de domínio e testes automatizados. Não há métricas de clientes, adoção ou desempenho de produção declaradas aqui.

---

## 🏛️ Arquitetura

Consulte [ARCHITECTURE.md](./ARCHITECTURE.md) para diagramas detalhados.

O diagrama e a dashboard descritos no documento são referências arquiteturais; o código público executável é o protótipo Python desta vitrine.

```
┌─────────────────┐         ┌─────────────────────────┐         ┌─────────────────┐
│   Fontes de     │         │   ETL Pipeline (Python) │         │   Angular 17    │
│   Dados         │────────►│   · Parse CSV           │────────►│   Dashboard     │
│   · ERP CSV     │         │   · Normalize           │         │   · 17 seções   │
│   · Bank CSV    │         │   · Validate            │         │   · TypeScript  │
│   · Support PDF │         │   · Analytical Engine   │         │   · RxJS        │
│   · GL CSV      │         │                         │         │                 │
└─────────────────┘         └─────────────────────────┘         └─────────────────┘
                                     │
                        ┌────────────▼────────────┐
                        │   Reconciliation Engine │
                        │   · Fuzzy Matching      │
                        │   · Risk Classification │
                        │   · ABC Analysis        │
                        │   · Aging Buckets       │
                        └─────────────────────────┘
```

---

## 🧪 Protótipo Educacional

Protótipo Python puro que demonstra as 6 análises principais com dados sintéticos:
- Aging Analysis
- Curva ABC
- Matriz de Risco
- Top Accounts
- Support Gap Detection
- Monthly Trend

```bash
cd prototype
python main.py
```

---

## ⚠️ Aviso Legal

**© 2026 Fernando Xavier. Todos os direitos reservados.**

Este repositório contém documentação arquitetural, protótipo educacional com dados 100% fictícios e imagens ilustrativas.

Nenhum dado de cliente ou resultado de produção está exposto.

---

<details>
<summary><sub>Stack técnico (para avaliadores técnicos)</sub></summary>

- **Protótipo executável:** Python 3.11 + biblioteca padrão
- **Dados:** seed determinístico gerado em `prototype/main.py`
- **Referência arquitetural:** ETL CSV, Angular e Docker são descritos como evolução possível, não como componentes deste protótipo

</details>

---

## 📬 Contato

[LinkedIn](https://linkedin.com/in/fernandoxavier02) · [FX Studio AI](https://fxstudioai.com)
