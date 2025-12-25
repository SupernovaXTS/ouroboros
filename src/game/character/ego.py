from __future__ import annotations
import attrs
@attrs.define
class Aptitude:
    """A class to represent a character's aptitude."""
    name: str
    level: int

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
class Aptitudes:
    """A class to hold all aptitudes for a character."""
    cognition: Aptitude
    intuition: Aptitude
    reflexes: Aptitude
    savvy: Aptitude
    somatics: Aptitude
    willpower: Aptitude
    def __init__(self) -> None:
        self.cognition = Aptitude(AptitudeNames.COGNITION, 0)
        self.intuition = Aptitude(AptitudeNames.INTUITION, 0)
        self.reflexes = Aptitude(AptitudeNames.REFLEXES, 0)
        self.savvy = Aptitude(AptitudeNames.SAVVY, 0)
        self.somatics = Aptitude(AptitudeNames.SOMATICS, 0)
        self.willpower = Aptitude(AptitudeNames.WILLPOWER, 0)

