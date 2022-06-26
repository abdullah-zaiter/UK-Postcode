from postcode.validator import Validator


def test_validate_postcode():
    assert Validator.is_valid_postcode("EC1A 1BB") is True
    assert Validator.is_valid_postcode("E1A 1BB") is True
    assert Validator.is_valid_postcode("W1A 0AX") is True
    assert Validator.is_valid_postcode("M1 1AE") is True
    assert Validator.is_valid_postcode("B33 8TH") is True
    assert Validator.is_valid_postcode("CR2 6XH") is True
    assert Validator.is_valid_postcode("DN55 1PT") is True

    assert Validator.is_valid_postcode("SADAKMxa da") is False
    assert Validator.is_valid_postcode("") is False
    assert Validator.is_valid_postcode("1C1A 1BB") is False
    assert Validator.is_valid_postcode("E122A 1BB") is False
    assert Validator.is_valid_postcode("EC1A 100") is False


def test_validate_area():
    assert Validator.is_valid_area("EC") is True
    assert Validator.is_valid_area("A") is True
    assert Validator.is_valid_area("a") is False
    assert Validator.is_valid_area("212") is False
    assert Validator.is_valid_area("") is False


def test_validate_district():
    assert Validator.is_valid_district("2") is True
    assert Validator.is_valid_district("21") is True
    assert Validator.is_valid_district("2A") is True
    assert Validator.is_valid_district("3B") is True

    assert Validator.is_valid_district("AB") is False
    assert Validator.is_valid_district("A2") is False
    assert Validator.is_valid_district("") is False


def test_validate_sector():
    assert Validator.is_valid_sector(2) is True
    assert Validator.is_valid_sector(0) is True
    assert Validator.is_valid_sector(9) is True

    assert Validator.is_valid_sector(-9) is False
    assert Validator.is_valid_sector(10) is False


def test_validate_unit():
    assert Validator.is_valid_unit("HF") is True
    assert Validator.is_valid_unit("AB") is True

    assert Validator.is_valid_unit("ab") is False
    assert Validator.is_valid_unit("") is False

