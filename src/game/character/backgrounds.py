"""Backgrounds Repository."""
from __future__ import annotations

import skills
from background import Background
from skill import SKILLRANGES

colonist = Background(
    "Colonist", "You were an original settler of Earth orbit, Luna, Mars, or a smaller outpost elsewhere, before the Fall.",
    {skills.freefall:SKILLRANGES(40),
     skills.base_hardware:SKILLRANGES(40),
     skills.interface:SKILLRANGES(30),
     skills.base_piloting:SKILLRANGES(30),
     skills.survival:SKILLRANGES(30),
     skills.base_know:SKILLRANGES(60),
     skills.base_know:SKILLRANGES(30)
    })

enclaver = Background(
    "Enclaver", "On Earth, you lived a life of precarious but protected stability in a defended enclave.",
    {
        skills.athletics:SKILLRANGES(40),
        skills.interface:SKILLRANGES(40),
        skills.kinesics:SKILLRANGES(30),
        skills.persuade:SKILLRANGES(20),
        skills.piloting.ground:SKILLRANGES(20),
        skills.program:SKILLRANGES(20),
        skills.base_know:SKILLRANGES(60),
        skills.base_know:SKILLRANGES(30),
    }
    )
