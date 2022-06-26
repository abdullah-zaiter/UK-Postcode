import re
from .postcode import Postcode


class Formatter:

    @staticmethod
    def from_string(postcode: str):
        area = ""
        district = ""
        sector = -1
        unit = ""

        match = re.search(
            "^(("
            "(?P<area>[A-Z]{1,2})"
            "(?P<district>[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA))"
            " ?"
            "(?P<sector>[0-9])"
            "(?P<unit>[A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1"
            "))$",
            postcode
        )

        if match:
            area = match.group("area")
            district = match.group("district")
            sector = int(match.group("sector"))
            unit = match.group("unit")

        return Postcode(area, district, sector, unit)
