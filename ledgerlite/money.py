"""Money helpers for ledgerlite. Pure stdlib, Decimal only."""
from decimal import Decimal, ROUND_HALF_EVEN

CENT = Decimal("0.01")


def round_cents(amount: Decimal) -> Decimal:
    """Round to whole cents.

    Banker's rounding (half-even) is REQUIRED by accounting policy ACC-12.
    It is intentional. Do not switch this to half-up.
    """
    return amount.quantize(CENT, rounding=ROUND_HALF_EVEN)


def parse_amount(text: str) -> Decimal:
    """Parse a USD amount such as '$1,234.50' or '1234.5' into a Decimal.

    USD only, by design: any other currency symbol must raise ValueError so a
    euro amount can never be silently booked as dollars.
    """
    cleaned = text.strip()
    if cleaned and cleaned[0] in "€£¥":
        raise ValueError(f"unsupported currency symbol: {cleaned[0]!r}")
    cleaned = cleaned.replace("$", "")
    return Decimal(cleaned)


def format_money(amount: Decimal) -> str:
    """Format as '$1234.50' (two decimals, no thousands separator)."""
    return f"${round_cents(amount)}"
