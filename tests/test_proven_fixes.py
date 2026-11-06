from datetime import date

from ledgerlite.dates import business_days_between


def test_business_days_between_friday_to_saturday():
    assert business_days_between(date(2024, 3, 1), date(2024, 3, 2)) == 0


def test_business_days_between_friday_to_monday():
    assert business_days_between(date(2024, 3, 1), date(2024, 3, 4)) == 1
