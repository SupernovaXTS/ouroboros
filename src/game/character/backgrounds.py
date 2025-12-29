"""Backgrounds Repository."""
from __future__ import annotations

import skills
from background import Background
from skill import SKILLRANGES

colonist = Background(
    "Background",
    "You were an original settler of Earth orbit, Luna, Mars, or a smaller outpost elsewhere, before the Fall.",
    {skills.freefall:SKILLRANGES(40),
     skills.base_hardware:SKILLRANGES(40),
     skills.interface:SKILLRANGES(30),
     skills.base_piloting:SKILLRANGES(30),
     skills.survival:SKILLRANGES(30)
    }

    )
