from datetime import date

from ledgerlite.dates import add_business_days, add_months, business_days_between


def test_add_months_mid_month():
    assert add_months(date(2024, 3, 15), 1) == date(2024, 4, 15)


def test_add_business_days_within_week():
    assert add_business_days(date(2024, 3, 4), 3) == date(2024, 3, 7)  # Mon -> Thu


def test_add_business_days_over_weekend():
    assert add_business_days(date(2024, 3, 1), 1) == date(2024, 3, 4)  # Fri -> Mon


def test_business_days_between_a_work_week():
    assert business_days_between(date(2024, 3, 4), date(2024, 3, 8)) == 4  # Mon -> Fri
