"""Background module for character management."""

from __future__ import annotations

from types import SimpleNamespace
from typing import TYPE_CHECKING

import attrs

if TYPE_CHECKING:
    from skill import SKILLRANGES, Skill

@attrs.define(eq=False)
class Background:
    """A class to represent a character's background."""
    name: str
    description: str
    skills: dict[Skill | SimpleNamespace, SKILLRANGES] = attrs.field(factory=dict)
    def __str__(self) -> str:
        """String representation of the Background."""
        return f"{self.name}: {self.description}"

@attrs.define(eq=False)
class Career:
    """A class to represent a character's career, this also controls gear packs."""
    name: str
    description: str
    skills: dict[Skill, SKILLRANGES] = attrs.field(factory=dict)
    def __str__(self) -> str:
        """String representation of the Career."""
        return f"{self.name}: {self.description}"

@attrs.define(eq=False)
class Interest:
    """A class to represent a character's interest."""
    name: str
    description: str
    skills: dict[Skill, SKILLRANGES] = attrs.field(factory=dict)
    def __str__(self) -> str:
        """String representation of the Career."""
        return f"{self.name}: {self.description}"
