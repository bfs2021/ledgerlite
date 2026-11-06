"""Small aggregations used by the monthly report."""
from collections import defaultdict
from decimal import Decimal
from typing import Dict, Iterable, List, Tuple

from .money import round_cents


def average_invoice(totals: List[Decimal]) -> Decimal:
    """Mean invoice total. An empty period averages to Decimal('0.00')."""
    return round_cents(sum(totals, Decimal("0")) / len(totals))


def top_customers(invoices: Iterable[Tuple[str, Decimal]], k: int) -> List[Tuple[str, Decimal]]:
    """Return the `k` customers with the largest combined spend, biggest first."""
    spend: Dict[str, Decimal] = defaultdict(lambda: Decimal("0"))
    for customer, total in invoices:
        spend[customer] += total
    ranked = sorted(spend.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:k]
