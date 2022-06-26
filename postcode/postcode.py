from dataclasses import dataclass

from postcode.validator import Validator


@dataclass
class Postcode:

    def __init__(self, area: str, district: str, sector: int, unit: str, validator: Validator = Validator) -> None:
        if not validator:
            raise ValueError("Invalid Validator")

        if not validator.is_valid_area(area):
            raise ValueError("Invalid area")

        if not validator.is_valid_district(district):
            raise ValueError("Invalid district")

        if not validator.is_valid_sector(sector):
            raise ValueError("Invalid sector")

        if not validator.is_valid_unit(unit):
            raise ValueError("Invalid unit")

        self.area = area
        self.district = district
        self.sector = sector
        self.unit = unit

        self.outward_code = area + district
        self.inward_code = str(sector) + unit
        self.full_postcode = self.outward_code + " " + self.inward_code

    def __str__(self):
        return f"""Formatted postcode "{self.full_postcode}":
        area: {self.area}
        district: {self.district}
        sector: {self.sector}
        unit: {self.unit}"""

    def __eq__(self, other):
        if (self.area == other.area) and (self.district == other.district) and (self.sector == other.sector) and (
                self.unit == other.unit):
            return True
        return False
