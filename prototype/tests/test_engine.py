"""Tests - Controllership Reconciliation Prototype."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from decimal import Decimal
from models import LedgerEntry
from engine import calculate_aging, calculate_abc, calculate_risk, reconcile


def test_aging_buckets():
    entries = [
        LedgerEntry(1, "1.1", "A", "AR", Decimal("1000"), "2026-01-01", 15, True, "NF-e"),
        LedgerEntry(2, "1.1", "B", "AR", Decimal("2000"), "2026-01-01", 45, True, "NF-e"),
        LedgerEntry(3, "1.1", "C", "AR", Decimal("3000"), "2026-01-01", 75, True, "NF-e"),
        LedgerEntry(4, "1.1", "D", "AR", Decimal("4000"), "2026-01-01", 100, True, "NF-e"),
    ]
    aging = calculate_aging(entries)
    assert len(aging) == 4
    assert aging[0].count == 1  # 0-30
    assert aging[3].count == 1  # 90+
    assert aging[3].total == Decimal("4000")


def test_abc_classification():
    entries = [
        LedgerEntry(1, "1.1", "A", "AR", Decimal("8000"), "2026-01-01", 0, True, "NF-e"),
        LedgerEntry(2, "1.1", "B", "AR", Decimal("1500"), "2026-01-01", 0, True, "NF-e"),
        LedgerEntry(3, "1.1", "C", "AR", Decimal("500"), "2026-01-01", 0, True, "NF-e"),
    ]
    abc = calculate_abc(entries)
    assert abc[0].classification == "A"  # 8000/10000 = 80%
    assert abc[0].count == 1
    assert abc[1].classification == "B"  # 1500/10000 = 15%
    assert abc[2].classification == "C"  # 500/10000 = 5%


def test_risk_classification():
    entries = [
        LedgerEntry(1, "1.1", "A", "AR", Decimal("150000"), "2026-01-01", 0, False, "NF-e"),
        LedgerEntry(2, "1.1", "B", "AR", Decimal("60000"), "2026-01-01", 0, False, "NF-e"),
        LedgerEntry(3, "1.1", "C", "AR", Decimal("10000"), "2026-01-01", 0, True, "NF-e"),
    ]
    risks = calculate_risk(entries)
    assert risks[0].risk_level == "ALTO"
    assert risks[1].risk_level == "MEDIO"
    assert risks[2].risk_level == "BAIXO"


def test_reconcile_totals():
    entries = [
        LedgerEntry(1, "1.1", "A", "AR", Decimal("1000"), "2026-01-01", 0, True, "NF-e"),
        LedgerEntry(2, "2.1", "B", "AP", Decimal("500"), "2026-01-01", 0, True, "NF-e"),
    ]
    result = reconcile(entries)
    assert result.total_entries == 2
    assert result.total_ar == Decimal("1000")
    assert result.total_ap == Decimal("500")


if __name__ == "__main__":
    test_aging_buckets()
    print("[PASS] test_aging_buckets")
    test_abc_classification()
    print("[PASS] test_abc_classification")
    test_risk_classification()
    print("[PASS] test_risk_classification")
    test_reconcile_totals()
    print("[PASS] test_reconcile_totals")
    print("\n[SUCCESS] All tests passed!")
