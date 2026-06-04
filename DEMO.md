# Demo — Protótipo Educacional Controllership Reconciliation

---

## Pré-requisitos

- Python 3.11+

---

## Execução

```bash
cd prototype
python main.py
```

---

## O que o protótipo faz

### Dados sintéticos pré-carregados

150 lançamentos contábeis fictícios (AR + AP) com:
- Valores entre R$ 1.000 e R$ 500.000
- Datas distribuídas nos últimos 90 dias
- 15% sem suporte documental (deliberado)
- 5 bancos fictícios

### Análises geradas

1. **Aging:** Distribuição por faixa de atraso
2. **ABC:** Classificação Pareto das contas
3. **Risk Matrix:** Alto/Médio/Baixo por valor + suporte
4. **Top 10:** Maiores contas por valor absoluto
5. **Support Gap:** Lançamentos sem documentação
6. **Monthly Trend:** Evolução de saldos

---

## Limitações vs. Produção

| Funcionalidade | Protótipo | Produção |
|---|---|---|
| Fonte de dados | JSON sintético | 8 CSVs reais do ERP |
| Frontend | Terminal/JSON | Angular 17 dashboard |
| Conciliação bancária | Simulada | Fuzzy matching real multi-banco |
| ETL | In-memory | Pipeline Dockerizado |
| Filtros contábeis | Genéricos | Hardcoded por cliente |
