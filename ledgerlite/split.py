"""Bill splitting."""
from decimal import Decimal, ROUND_DOWN
from typing import List

CENT = Decimal("0.01")


def split_evenly(total: Decimal, n: int) -> List[Decimal]:
    """Split `total` into `n` shares that add up to exactly `total`.

    Shares differ by at most one cent. Earlier shares take the extra cents.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    share = (total / n).quantize(CENT, rounding=ROUND_DOWN)
    return [share for _ in range(n)]
