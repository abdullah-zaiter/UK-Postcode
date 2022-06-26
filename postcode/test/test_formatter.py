from postcode.formatter import Formatter
from postcode.postcode import Postcode


def test_postcode_formatting_matching():
    assert Postcode(area="AZ", district="3C", sector=3, unit="CC") == Formatter.from_string("AZ3C 3CC")


def test_postcode_formatting_not_matching():
    assert Postcode(area="AZ", district="3C", sector=3, unit="CC") != Formatter.from_string("AY3C 3CC")
