from decimal import Decimal

from ledgerlite.invoice import Line, invoice_total, line_total, quote_total


def test_line_total_without_discount():
    assert line_total(Line("A", Decimal("9.99"), 3)) == Decimal("29.97")


def test_line_total_with_discount():
    assert line_total(Line("A", Decimal("100.00"), 2, Decimal("10"))) == Decimal("180.00")


def test_invoice_total_simple_tax():
    lines = [Line("A", Decimal("10.00"), 2), Line("B", Decimal("5.00"), 1)]
    assert invoice_total(lines, Decimal("0.10")) == Decimal("27.50")


def test_quote_matches_invoice_when_no_discount():
    lines = [Line("A", Decimal("10.00"), 2), Line("B", Decimal("5.00"), 1)]
    assert quote_total(lines, Decimal("0.10")) == invoice_total(lines, Decimal("0.10"))
