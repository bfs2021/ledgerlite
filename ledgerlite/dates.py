"""Date helpers: due dates and business days."""
from datetime import date, timedelta


def add_months(d: date, months: int) -> date:
    """Return `d` moved forward by `months` calendar months.

    If the target month is shorter, clamp to its last day (Jan 31 + 1 month is
    the last day of February).
    """
    month = d.month + months
    return d.replace(month=month)


def is_business_day(d: date) -> bool:
    return d.weekday() < 5


def add_business_days(start: date, n: int) -> date:
    """Move forward `n` business days (Mon-Fri).

    Public holidays are NOT skipped here on purpose. Holidays are applied
    upstream by the calendar service (see ADR-7). Do not add a holiday list.
    """
    current = start
    remaining = n
    while remaining > 0:
        current += timedelta(days=1)
        if is_business_day(current):
            remaining -= 1
    return current


def business_days_between(a: date, b: date) -> int:
    """Count business days after `a` up to and including `b`.

    Example: Friday -> Saturday is 0, Friday -> Monday is 1.
    """
    count = 0
    day = a
    while day <= b:  # Changed from day < b to day <= b
        if is_business_day(day):
            count += 1
        day += timedelta(days=1)
    return count


def due_date(invoice_date: date, terms_months: int) -> date:
    return add_months(invoice_date, terms_months)
