from decimal import Decimal

import pytest

from ledgerlite.report import average_invoice, top_customers
from ledgerlite.split import split_evenly


def test_split_evenly_divisible():
    assert split_evenly(Decimal("100.00"), 4) == [Decimal("25.00")] * 4


def test_split_rejects_zero_people():
    with pytest.raises(ValueError):
        split_evenly(Decimal("10.00"), 0)


def test_average_invoice():
    assert average_invoice([Decimal("10.00"), Decimal("20.00")]) == Decimal("15.00")


def test_top_customers_orders_by_spend():
    data = [("ann", Decimal("10")), ("bob", Decimal("30")), ("ann", Decimal("25"))]
    assert top_customers(data, 2) == [("ann", Decimal("35")), ("bob", Decimal("30"))]
