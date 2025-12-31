"""Skill class definition module."""
from __future__ import annotations

import copy
from enum import IntEnum
from types import SimpleNamespace
from typing import TYPE_CHECKING

import attrs

if TYPE_CHECKING:
    from ego import Aptitude


def skillfield(baseskill: Skill, fields: list[str]) -> SimpleNamespace:
    """Taking a base skill and a list of fields, return a list of skills with those fields."""
    skills = {}
    for field in fields:
        assign = field.lower()
        skill = copy.deepcopy(baseskill)
        skill.field = field
        skills[assign] = skill
    return SimpleNamespace(**skills)
class SKILLRANGES(IntEnum):
    """Enum to represent skill proficiency levels."""
    UNTRAINED = 0
    RUDIMENTARY = 10
    SOMEWHAT_SKILLED = 20
    NOVICE = 30
    COMPETENT = 40
    ADVANCED = 50
    EXPERIENCED = 60
    EXPERT = 70
    AUTHORITY = 80
    MASTER = 90
    LEGENDARY = 100

@attrs.define(eq=False)
class Skill:
    """A class to represent a character's skill."""
    name: str
    associated_aptitude: Aptitude
    types: list[str] = attrs.field(factory=list)
    options: list[str] = attrs.field(factory=list)
    level: IntEnum = SKILLRANGES.UNTRAINED # By default skills start untrained, we will assign levels later in character creation
    field: str | None = None
    def __str__(self) -> str:
        """String representation of the Skill."""
        if self.field:
            return f"{self.name}:({self.field}) (Level: {SKILLRANGES(self.level).name}, Aptitude: {self.associated_aptitude})"
        return f"{self.name} (Level: {SKILLRANGES(self.level).name}, Aptitude: {self.associated_aptitude.name})"
    def spec(self,level: IntEnum) -> Skill:
        """Return a new Skill with the specified level."""
        new_skill = copy.deepcopy(self)
        new_skill.level = level
        return new_skill

