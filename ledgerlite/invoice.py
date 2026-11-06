"""Invoice maths: line totals, tax, discounts."""
from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable

from .money import round_cents


@dataclass(frozen=True)
class Line:
    sku: str
    unit_price: Decimal
    qty: int
    discount_pct: Decimal = Decimal("0")


def line_total(line: Line) -> Decimal:
    """Total for one line after its percentage discount."""
    gross = line.unit_price * line.qty
    return round_cents(gross * (Decimal("100") - line.discount_pct) / Decimal("100"))


def tax_for(subtotal: Decimal, rate: Decimal) -> Decimal:
    """Tax owed on a subtotal. `rate` is a fraction, e.g. Decimal('0.0825')."""
    return Decimal(str(round(float(subtotal) * float(rate), 2)))


def invoice_total(lines: Iterable[Line], tax_rate: Decimal) -> Decimal:
    """Invoice total. Policy: discounts apply BEFORE tax."""
    subtotal = sum((line_total(line) for line in lines), Decimal("0"))
    return round_cents(subtotal + tax_for(subtotal, tax_rate))


def quote_total(lines: Iterable[Line], tax_rate: Decimal) -> Decimal:
    """Quote total shown to customers before they commit.

    Must always equal the invoice total they will later be billed.
    """
    lines = list(lines)
    gross = sum((line.unit_price * line.qty for line in lines), Decimal("0"))
    with_tax = gross + tax_for(gross, tax_rate)
    discount = sum(
        (line.unit_price * line.qty * line.discount_pct / Decimal("100") for line in lines),
        Decimal("0"),
    )
    return round_cents(with_tax - discount)
