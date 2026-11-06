from decimal import Decimal

from ledgerlite.invoice import Line, invoice_total, line_total, quote_total, tax_for


def test_line_total_without_discount():
    assert line_total(Line("A", Decimal("9.99"), 3)) == Decimal("29.97")


def test_line_total_with_discount():
    assert line_total(Line("A", Decimal("100.00"), 2, Decimal("10"))) == Decimal("180.00")


def test_invoice_total_simple_tax():
    lines = [Line("A", Decimal("10.00"), 2), Line("B", Decimal("5.00"), 1)]
    assert invoice_total(lines, Decimal("0.10")) == Decimal("27.50")


def test_tax_for_uses_exact_decimal_bankers_rounding():
    # Policy ACC-12: tax is computed with exact Decimal maths and round_cents.
    # 2.00 * 0.0825 = 0.165 exactly; a half-even tie goes to 0.16, not 0.17.
    assert tax_for(Decimal("2.00"), Decimal("0.0825")) == Decimal("0.16")


def test_tax_for_exact_decimal_no_float_drift():
    # 0.10 * 3 = 0.30 exactly; a float path can land one cent off on such ties.
    assert tax_for(Decimal("3.00"), Decimal("0.10")) == Decimal("0.30")


def test_quote_matches_invoice_when_no_discount():
    lines = [Line("A", Decimal("10.00"), 2), Line("B", Decimal("5.00"), 1)]
    assert quote_total(lines, Decimal("0.10")) == invoice_total(lines, Decimal("0.10"))
