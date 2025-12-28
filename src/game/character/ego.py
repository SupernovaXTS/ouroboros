"""Player Ego Module."""
from __future__ import annotations

from enum import IntEnum

import attrs


@attrs.define
class Aptitude:
    """A class to represent a character's aptitude."""
    name: str
    abreviation: str
    level: IntEnum

@attrs.define
class AptitudeNames:
    """Class to hold aptitude name constants."""
    COGNITION: str = "Cognition"
    INTUITION: str = "Intuition"
    REFLEXES: str = "Reflexes"
    SAVVY: str = "Savvy"
    SOMATICS: str = "Somatics"
    WILLPOWER: str = "Willpower"
@attrs.define
class AptitudeAbreviations:
    """Enum to represent aptitude abbreviations."""
    COG: str = "COG"
    INT: str = "INT"
    REF: str = "REF"
    SAV: str = "SAV"
    SOM: str = "SOM"
    WIL: str = "WIL"

class AptitudeAssessment(IntEnum):
    """Enum to represent aptitude assessment levels."""
    INCAPABLE = 0
    CHILD = 5
    BASELINE = 10
    TRANSHUMAN = 15
    ENHANCED = 20
    SUPERHUMAN = 25
    POSTHUMAN = 30

@attrs.define
class Aptitudes:
    """A class to hold all aptitudes for a ego."""
    cognition: Aptitude
    intuition: Aptitude
    reflexes: Aptitude
    savvy: Aptitude
    somatics: Aptitude
    willpower: Aptitude
    def __init__(self) -> None:
        """Initialize all aptitudes to level 5."""
        self.cognition = Aptitude(AptitudeNames.COGNITION, AptitudeAbreviations.COG, AptitudeAssessment.CHILD)
        self.intuition = Aptitude(AptitudeNames.INTUITION, AptitudeAbreviations.INT, AptitudeAssessment.CHILD)
        self.reflexes = Aptitude(AptitudeNames.REFLEXES, AptitudeAbreviations.REF, AptitudeAssessment.CHILD)
        self.savvy = Aptitude(AptitudeNames.SAVVY, AptitudeAbreviations.SAV, AptitudeAssessment.CHILD)
        self.somatics = Aptitude(AptitudeNames.SOMATICS, AptitudeAbreviations.SOM, AptitudeAssessment.CHILD)
        self.willpower = Aptitude(AptitudeNames.WILLPOWER, AptitudeAbreviations.WIL, AptitudeAssessment.CHILD)

