"""Models - Controllership Reconciliation Prototype."""

from dataclasses import dataclass
from typing import List
from decimal import Decimal


@dataclass
class LedgerEntry:
    id: int
    account_code: str
    account_name: str
    type: str  # AR or AP
    amount: Decimal
    date: str
    days_overdue: int
    has_support: bool
    document_type: str
    bank: str = ""


@dataclass
class AgingBucket:
    range_label: str
    count: int
    total: Decimal


@dataclass
class ABCClass:
    classification: str  # A, B, C
    count: int
    total: Decimal
    percentage: Decimal


@dataclass
class RiskEntry:
    account_code: str
    account_name: str
    amount: Decimal
    has_support: bool
    risk_level: str  # ALTO, MEDIO, BAIXO


@dataclass
class ReconciliationSummary:
    total_entries: int
    total_ar: Decimal
    total_ap: Decimal
    aging_buckets: List[AgingBucket]
    abc_classes: List[ABCClass]
    risk_entries: List[RiskEntry]
    top_accounts: List[dict]
    support_gaps: List[LedgerEntry]
    monthly_trend: List[dict]
