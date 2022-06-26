import re

validation_types = ["postcode", "area", "district", "sector", "unit"]


class Validator:

    @staticmethod
    def is_valid_postcode(postcode: str) -> bool:
        result = bool(re.match(
            ("^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}"
             "|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$")
            , postcode
        ))
        return result

    @staticmethod
    def is_valid_area(area: str):
        result = bool(re.match(
            "[A-Z]{1,2}",
            area
        ))
        return result

    @staticmethod
    def is_valid_district(district: str):
        result = bool(re.match(
            "[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA",
            district
        ))
        return result

    @staticmethod
    def is_valid_sector(sector: int):
        try:
            sector = int(sector)
        except ValueError:
            return False

        result = True if (sector >= 0) & (sector <= 9) else False
        return result

    @staticmethod
    def is_valid_unit(unit: str):
        result = bool(re.match(
            "[A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1",
            unit
        ))
        return result
