from decimal import Decimal

import pytest

from ledgerlite.money import format_money, parse_amount, round_cents


def test_round_cents_uses_bankers_rounding():
    # Policy ACC-12: ties go to the even cent.
    assert round_cents(Decimal("0.125")) == Decimal("0.12")
    assert round_cents(Decimal("0.135")) == Decimal("0.14")


def test_round_cents_plain_value():
    assert round_cents(Decimal("3.14159")) == Decimal("3.14")


def test_parse_amount_with_dollar_sign():
    assert parse_amount("$12.50") == Decimal("12.50")


def test_parse_amount_plain_number():
    assert parse_amount("12") == Decimal("12")


def test_format_money_pads_to_two_decimals():
    assert format_money(Decimal("5")) == "$5.00"
