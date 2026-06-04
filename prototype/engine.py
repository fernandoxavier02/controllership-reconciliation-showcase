"""Engine - Controllership Reconciliation Prototype."""

from decimal import Decimal
from typing import List
from models import LedgerEntry, AgingBucket, ABCClass, RiskEntry, ReconciliationSummary


def calculate_aging(entries: List[LedgerEntry]) -> List[AgingBucket]:
    buckets = {
        "0-30 dias": [],
        "31-60 dias": [],
        "61-90 dias": [],
        "90+ dias": [],
    }
    for e in entries:
        if e.days_overdue <= 30:
            buckets["0-30 dias"].append(e)
        elif e.days_overdue <= 60:
            buckets["31-60 dias"].append(e)
        elif e.days_overdue <= 90:
            buckets["61-90 dias"].append(e)
        else:
            buckets["90+ dias"].append(e)

    return [
        AgingBucket(label, len(items), sum(e.amount for e in items))
        for label, items in buckets.items()
    ]


def calculate_abc(entries: List[LedgerEntry]) -> List[ABCClass]:
    sorted_entries = sorted(entries, key=lambda e: e.amount, reverse=True)
    total = sum(e.amount for e in entries)
    if total == 0:
        return []

    cumulative = Decimal("0")
    a_total, b_total, c_total = Decimal("0"), Decimal("0"), Decimal("0")
    a_count, b_count, c_count = 0, 0, 0

    for e in sorted_entries:
        cumulative += e.amount
        pct = cumulative / total * 100
        if pct <= 80:
            a_total += e.amount
            a_count += 1
        elif pct <= 95:
            b_total += e.amount
            b_count += 1
        else:
            c_total += e.amount
            c_count += 1

    return [
        ABCClass("A", a_count, a_total, a_total / total * 100),
        ABCClass("B", b_count, b_total, b_total / total * 100),
        ABCClass("C", c_count, c_total, c_total / total * 100),
    ]


def calculate_risk(entries: List[LedgerEntry]) -> List[RiskEntry]:
    risks = []
    for e in entries:
        if e.amount >= Decimal("100000") and not e.has_support:
            level = "ALTO"
        elif e.amount >= Decimal("50000") and not e.has_support:
            level = "MEDIO"
        elif not e.has_support:
            level = "BAIXO"
        else:
            level = "BAIXO"
        risks.append(RiskEntry(e.account_code, e.account_name, e.amount, e.has_support, level))
    return risks


def get_top_accounts(entries: List[LedgerEntry], n: int = 10) -> List[dict]:
    sorted_entries = sorted(entries, key=lambda e: abs(e.amount), reverse=True)
    return [
        {"account_code": e.account_code, "account_name": e.account_name, "amount": e.amount}
        for e in sorted_entries[:n]
    ]


def get_support_gaps(entries: List[LedgerEntry]) -> List[LedgerEntry]:
    return [e for e in entries if not e.has_support]


def get_monthly_trend(entries: List[LedgerEntry]) -> List[dict]:
    from collections import defaultdict
    months = defaultdict(lambda: {"ar": Decimal("0"), "ap": Decimal("0")})
    for e in entries:
        month = e.date[:7]  # YYYY-MM
        if e.type == "AR":
            months[month]["ar"] += e.amount
        else:
            months[month]["ap"] += e.amount
    return [{"month": m, **v} for m, v in sorted(months.items())]


def reconcile(entries: List[LedgerEntry]) -> ReconciliationSummary:
    ar_entries = [e for e in entries if e.type == "AR"]
    ap_entries = [e for e in entries if e.type == "AP"]

    return ReconciliationSummary(
        total_entries=len(entries),
        total_ar=sum(e.amount for e in ar_entries),
        total_ap=sum(e.amount for e in ap_entries),
        aging_buckets=calculate_aging(entries),
        abc_classes=calculate_abc(entries),
        risk_entries=calculate_risk(entries),
        top_accounts=get_top_accounts(entries),
        support_gaps=get_support_gaps(entries),
        monthly_trend=get_monthly_trend(entries),
    )
