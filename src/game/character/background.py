"""Background module for character management."""

from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING

import attrs

if TYPE_CHECKING:
    from skill import Skill

@attrs.define
class Background:
    """A class to represent a character's background."""
    name: str
    description: str
    starting_skills: dict[Skill, IntEnum] = attrs.field(factory=dict)
    def __str__(self) -> str:
        """String representation of the Background."""
        return f"{self.name}: {self.description}"
