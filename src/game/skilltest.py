"""Docstring for game.skilltest."""
from __future__ import annotations
from enum import Enum
import random

import attrs


class Modifier(Enum):
    """Enum for difficulty levels."""
    very_easy = 30
    easy = 20
    slightly_easy = 10
    average = 0
    slightly_hard = -10
    hard = -20
    very_hard = -30

class CheckResult(Enum):
    """Enum for skill check results."""
    critical_failure = -2
    failure = -1
    neutral = 0
    success = 1
    critical_success = 2


@attrs.define
class checkOutcome:
    """A class to represent the outcome of a skill check."""
    result: CheckResult
    message: str
    success: bool
    superiorSuccess: int
    superiorFailure: int

@attrs.define
class SkillCheck:
    """A class to represent a skill check."""
    skill_name: str
    skill_level: int
    modifier: int
    difficulty: int
    success_message: str
    failure_message: str

def analyze_roll(roll: int, skill_check: SkillCheck) -> CheckResult:
    """Analyze the roll and return the check result."""
    if roll == 00:
        return CheckResult.critical_success
    elif roll == 99:
        return CheckResult.critical_failure
    crits = [11, 22, 33, 44, 55, 66, 77, 88]
    check = skill_check.difficulty + skill_check.modifier
    if roll in crits:
        if roll <= check:
            return CheckResult.critical_success
        else:
            return CheckResult.critical_failure
    else:
        if roll <= check:
            return CheckResult.success
        else:
            return CheckResult.failure
def superior(roll:int, skill_check: SkillCheck, result: CheckResult) -> list[int]:
    superior_success = 0
    superior_failure = 0
    if (result == CheckResult.success or result == CheckResult.critical_success):
        if roll >= 33:
            superior_success += 1
        if roll >= 66:
            superior_success += 1
    elif (result == CheckResult.failure or result == CheckResult.critical_failure):
        if roll <= 66:
            superior_failure += 1
        if roll <= 33:
            superior_failure += 1
    return [superior_success, superior_failure]

def perform_skill_check(skill_check: SkillCheck) -> checkOutcome:
    """Perform a skill check and return the result."""
    roll1 = str(random.randint(0,9))
    roll2 = str(random.randint(0,9))
    roll = int(roll1 + roll2)
    result = analyze_roll(roll, skill_check)
    superior_results = superior(roll, skill_check, result)
    if result == CheckResult.success or result == CheckResult.critical_success:
        message = skill_check.success_message
        success = True
    else:
        message = skill_check.failure_message
        success = False

    outcome = checkOutcome(
        result=result,
        message=message,
        success=success,
        superiorSuccess=superior_results[0],
        superiorFailure=superior_results[1]
    )
    return outcome
    