"""Module for managing character aptitudes and assessments."""
from __future__ import annotations

from ego import AptitudeAssessment, Aptitudes

actioneer = Aptitudes().spec(
    cognition=AptitudeAssessment.BASELINE, intuition=AptitudeAssessment.TRANSHUMAN,
    reflexes=AptitudeAssessment.ENHANCED, savvy=AptitudeAssessment.BASELINE,
    somatics=AptitudeAssessment(20), willpower=AptitudeAssessment(15)
)

extrovert = Aptitudes().spec(
    cognition=AptitudeAssessment(10),intuition=AptitudeAssessment(20),
    reflexes=AptitudeAssessment(15),savvy=AptitudeAssessment(20),
    somatics=AptitudeAssessment(15),willpower=AptitudeAssessment(10)
)

facilitator = Aptitudes().spec(
    cognition=AptitudeAssessment(15), intuition=AptitudeAssessment(15),
    reflexes=AptitudeAssessment(10), savvy=AptitudeAssessment(20),
    somatics=AptitudeAssessment(10), willpower=AptitudeAssessment(20)
)

factotum = Aptitudes().spec(
    cognition=AptitudeAssessment(15), intuition=AptitudeAssessment(15),
    reflexes=AptitudeAssessment(15), savvy=AptitudeAssessment(15),
    somatics=AptitudeAssessment(15), willpower=AptitudeAssessment(15)
)

inquirer = Aptitudes().spec(
    cognition=AptitudeAssessment(20), intuition=AptitudeAssessment(20),
    reflexes=AptitudeAssessment(10), savvy=AptitudeAssessment(15),
    somatics=AptitudeAssessment(10), willpower=AptitudeAssessment(15)
)

survivor = Aptitudes().spec(
    cognition=AptitudeAssessment(15), intuition=AptitudeAssessment(10),
    reflexes=AptitudeAssessment(15), savvy=AptitudeAssessment(10),
    somatics=AptitudeAssessment(20), willpower=AptitudeAssessment(20)
)

thrill_seeker = Aptitudes().spec(
    cognition=AptitudeAssessment(20), intuition=AptitudeAssessment(10),
    reflexes=AptitudeAssessment(20), savvy=AptitudeAssessment(15),
    somatics=AptitudeAssessment(15), willpower=AptitudeAssessment(10)
)
