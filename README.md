# Controllership Reconciliation Engine — Showcase

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Domain: Financial Engineering](https://img.shields.io/badge/Domain-AR%2FAP_Reconciliation-412991.svg?style=for-the-badge)](https://github.com/fernandoxavier02)
[![FX Studio AI](https://img.shields.io/badge/FX_Studio_AI-Finance_Architecture-FF6B6B?style=for-the-badge)](https://github.com/fernandoxavier02)

**Architectural showcase and analytical engine for AR/AP aging, Pareto ABC classification, risk matrices, support gap detection, and monthly trends.**

</div>

---

## 🌟 Executive Overview

Financial controllership and operations teams must reconcile transactions across **Accounts Receivable (AR)**, **Accounts Payable (AP)**, **Bank Statements**, and the **General Ledger (GL)**.

Without explicit rules and automated reconciliations, teams face delayed month-end close cycles, audit frictions, and reliance on untracked spreadsheets. This showcase provides an automated analytical Python engine executing six core financial controllership workflows.

---

## 🏗️ Core Analytical Modules

| Module | Description | Impact |
| :--- | :--- | :--- |
| **Aging Analysis** | Bucket categorization (0–30, 31–60, 61–90, 90+ days past due) | Prioritized collection and payment schedules |
| **ABC Pareto Curve** | Value-based concentration (A = top 80%, B = 15%, C = 5%) | Exception-based risk governance |
| **Risk Matrix** | High/Medium/Low exposure classification combining value and documentation | Objective audit risk scoring |
| **Top 10 Exposure** | Highest absolute exposure accounts | Focus on material balances |
| **Support Gap Detection** | Automated discovery of entries lacking supporting documentation | Closes audit trail vulnerabilities |
| **Monthly Trend Engine** | Multi-period AR/AP volume and cash movement evolution | Working capital visibility |

---

## 🏛️ System Architecture

```
┌─────────────────┐         ┌─────────────────────────┐         ┌─────────────────┐
│  Data Sources   │         │   ETL Pipeline (Python) │         │  Dashboard UI   │
│  · ERP CSV      │────────►│   · Parser & Normalizer │────────►│  · Analytical   │
│  · Bank Feeds   │         │   · Validator           │         │  · Visual Heat  │
│  · GL Balances  │         │   · Analytical Engine   │         │    Maps & KPIs  │
└─────────────────┘         └─────────────────────────┘         └─────────────────┘
                                     │
                        ┌────────────▼────────────┐
                        │  Reconciliation Core   │
                        │  · Fuzzy Matching       │
                        │  · Risk Classification  │
                        │  · ABC & Aging Buckets  │
                        └─────────────────────────┘
```

---

## 🧪 Educational Prototype Quickstart

This repository contains a standalone, pure Python 3.11 analytical engine with deterministic fixtures demonstrating all six controllership calculations:

```bash
cd prototype
python main.py
```

The script executes the full suite of reconciliations, computes aging brackets, performs ABC Pareto breakdowns, and outputs tabular audit matrices to stdout.

---

## 📄 License & Attribution

- **Author:** [Fernando Xavier](https://github.com/fernandoxavier02) — *Founder, FX Studio AI | Finance Executive*
- **License:** [MIT License](LICENSE)
