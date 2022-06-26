from postcode.postcode import Postcode
import pytest


def test_postcode_invalid_areas():

    with pytest.raises(ValueError, match="Invalid area"):
        Postcode(area="1C", district="1A", sector=1, unit="BB")

    with pytest.raises(ValueError, match="Invalid area"):
        Postcode(area="2", district="1A", sector=1, unit="BB")

    with pytest.raises(ValueError, match="Invalid area"):
        Postcode(area="", district="1A", sector=1, unit="BB")


def test_postcode_invalid_districts():

    with pytest.raises(ValueError, match="Invalid district"):
        Postcode(area="EC", district="A", sector=1, unit="BB")

    with pytest.raises(ValueError, match="Invalid district"):
        Postcode(area="EC", district="", sector=1, unit="BB")


def test_postcode_invalid_sectors():

    with pytest.raises(ValueError, match="Invalid sector"):
        Postcode(area="EC", district="1A", sector=-1, unit="BB")

    with pytest.raises(ValueError, match="Invalid sector"):
        Postcode(area="EC", district="1A", sector=10, unit="BB")


def test_postcode_invalid_units():

    with pytest.raises(ValueError, match="Invalid unit"):
        Postcode(area="EC", district="1A", sector=1, unit="1B")

    with pytest.raises(ValueError, match="Invalid unit"):
        Postcode(area="EC", district="1A", sector=1, unit="12")

    with pytest.raises(ValueError, match="Invalid unit"):
        Postcode(area="EC", district="1A", sector=1, unit="B2")

    with pytest.raises(ValueError, match="Invalid unit"):
        Postcode(area="EC", district="1A", sector=1, unit="")
