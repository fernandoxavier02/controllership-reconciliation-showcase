"""Main - Controllership Reconciliation Prototype."""

import json
from decimal import Decimal
from models import LedgerEntry
from engine import reconcile


def generate_seed_data() -> list[LedgerEntry]:
    """Generate 100% synthetic ledger entries."""
    accounts_ar = [
        ("1.1.02.01.01.001", "Cliente A - Distribuidora"),
        ("1.1.02.01.01.002", "Cliente B - Varejo"),
        ("1.1.02.01.01.003", "Cliente C - Industria"),
        ("1.1.02.01.01.004", "Cliente D - Servicos"),
        ("1.1.02.01.01.005", "Cliente E - Exportacao"),
    ]
    accounts_ap = [
        ("2.1.01.01.01.001", "Fornecedor X - Materia Prima"),
        ("2.1.01.01.01.002", "Fornecedor Y - Logistica"),
        ("2.1.01.01.01.003", "Fornecedor Z - Tecnologia"),
        ("2.1.01.01.01.004", "Fornecedor W - Energia"),
        ("2.1.01.01.01.005", "Fornecedor V - Manutencao"),
    ]

    import random
    random.seed(42)
    entries = []

    for i in range(150):
        is_ar = random.random() < 0.45
        accounts = accounts_ar if is_ar else accounts_ap
        code, name = random.choice(accounts)
        amount = Decimal(str(round(random.uniform(1000, 500000), 2)))
        days = random.randint(0, 120)
        has_support = random.random() > 0.15
        doc_types = ["NF-e", "Boleto", "Fatura", "Recibo", "Contrato", "DS"]
        doc = random.choice(doc_types)
        date = f"2026-{random.randint(1,5):02d}-{random.randint(1,28):02d}"

        entries.append(LedgerEntry(
            id=i+1,
            account_code=code,
            account_name=name,
            type="AR" if is_ar else "AP",
            amount=amount,
            date=date,
            days_overdue=days,
            has_support=has_support,
            document_type=doc,
            bank=random.choice(["BMG", "Citi", "Bradesco", "Itau", "Santander"]) if not is_ar else "",
        ))
    return entries


def main():
    print("=" * 70)
    print("Controllership Reconciliation Engine - Prototype")
    print("=" * 70)

    entries = generate_seed_data()
    result = reconcile(entries)

    print(f"\n>>> Resumo Geral")
    print(f"    Total de Lançamentos: {result.total_entries}")
    print(f"    Total AR: R$ {result.total_ar:,.2f}")
    print(f"    Total AP: R$ {result.total_ap:,.2f}")

    print(f"\n>>> Aging de Contas")
    for b in result.aging_buckets:
        print(f"    {b.range_label:12} | {b.count:4} lançamentos | R$ {b.total:>12,.2f}")

    print(f"\n>>> Curva ABC")
    for c in result.abc_classes:
        print(f"    Classe {c.classification} | {c.count:4} contas | R$ {c.total:>12,.2f} ({c.percentage:.1f}%)")

    print(f"\n>>> Matriz de Risco (Top 5)")
    for r in sorted(result.risk_entries, key=lambda x: x.amount, reverse=True)[:5]:
        support = "OK" if r.has_support else "SEM SUPORTE"
        print(f"    [{r.risk_level:5}] {r.account_name:30} | R$ {r.amount:>10,.2f} | {support}")

    print(f"\n>>> Lançamentos sem Suporte Documental: {len(result.support_gaps)}")

    print(f"\n>>> Tendência Mensal")
    for t in result.monthly_trend:
        print(f"    {t['month']} | AR: R$ {t['ar']:>10,.2f} | AP: R$ {t['ap']:>10,.2f}")

    print("\n" + "=" * 70)
    print("Prototype execution completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
