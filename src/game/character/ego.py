"""Player Ego Module."""
from __future__ import annotations

from enum import IntEnum
from types import SimpleNamespace
from typing import TYPE_CHECKING

import attrs

if TYPE_CHECKING:
    from game.character.background import Background, Career, Interest

@attrs.define(eq=False)
class AptitudeNames:
    """Class to hold aptitude name constants."""
    COGNITION: str = "Cognition"
    INTUITION: str = "Intuition"
    REFLEXES: str = "Reflexes"
    SAVVY: str = "Savvy"
    SOMATICS: str = "Somatics"
    WILLPOWER: str = "Willpower"
@attrs.define(eq=False)
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

@attrs.define(eq=False)
class Aptitude:
    """A class to represent a character's aptitude."""
    name: str
    abreviation: str
    level: AptitudeAssessment = AptitudeAssessment.CHILD
    def spec(self,level:AptitudeAssessment) -> None:
        """Set an aptitude to an level."""
        self.level = level
    def __str__(self) -> str:
        """Docstring for __str__.

        :param self: Description
        :return: Description
        :rtype: str
        """
        return f"{self.name}:{self.level}"


@attrs.define(eq=False)
class Aptitudes:
    """A class to hold all aptitudes for a ego."""
    cognition: Aptitude = attrs.field(default=Aptitude(AptitudeNames.COGNITION, AptitudeAbreviations.COG, AptitudeAssessment.CHILD))
    intuition: Aptitude = attrs.field(default=Aptitude(AptitudeNames.INTUITION, AptitudeAbreviations.INT, AptitudeAssessment.CHILD))
    reflexes: Aptitude = attrs.field(default=Aptitude(AptitudeNames.REFLEXES, AptitudeAbreviations.REF, AptitudeAssessment.CHILD))
    savvy: Aptitude = attrs.field(default=Aptitude(AptitudeNames.SAVVY, AptitudeAbreviations.SAV, AptitudeAssessment.CHILD))
    somatics: Aptitude = attrs.field(default=Aptitude(AptitudeNames.SOMATICS, AptitudeAbreviations.SOM, AptitudeAssessment.CHILD))
    willpower: Aptitude = attrs.field(default=Aptitude(AptitudeNames.WILLPOWER, AptitudeAbreviations.WIL, AptitudeAssessment.CHILD))
    def spec(self,cognition: AptitudeAssessment,intuition: AptitudeAssessment,reflexes: AptitudeAssessment,savvy: AptitudeAssessment,somatics:AptitudeAssessment,willpower:AptitudeAssessment) -> None:
        """Set all aptitudes to specified levels.

        Parameters
        ----------
        cognition : AptitudeAssessment
            Cognition aptitude level.
        intuition : AptitudeAssessment
            Intuition aptitude level.
        reflexes : AptitudeAssessment
            Reflexes aptitude level.
        savvy : AptitudeAssessment
            Savvy aptitude level.
        somatics : AptitudeAssessment
            Somatics aptitude level.
        willpower : AptitudeAssessment
            Willpower aptitude level.
        """
        self.cognition.spec(cognition)
        self.intuition.spec(intuition)
        self.reflexes.spec(reflexes)
        self.savvy.spec(savvy)
        self.somatics.spec(somatics)
        self.willpower.spec(willpower)
@attrs.define(eq=False)
class Ego:
    """Container for character ego data."""
    name: str
    aptitudes: Aptitudes
    skills: SimpleNamespace
    background: Background
    career: Career
    interest: Interest

