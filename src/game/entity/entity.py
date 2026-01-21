"""Module for entity handling."""
from __future__ import annotations

import attrs
import mcrfpy  # pyright: ignore[reportMissingModuleSource]

from game import constants


@attrs.define
class Entity(mcrfpy.Entity):
    """Base Class for entities."""
    weight: float = 0.0 * constants.ureg.gram  # Weight of the entity in grams
    length: float = 0.0 * constants.ureg.centimeter  # Length of the entity in centimeters
    width: float = 0.0 * constants.ureg.centimeter  # Width of the entity in centimeters
    depth: float = 0.0 * constants.ureg.centimeter  # Depth of the entity in centimeters
    volume: float = 0.0 * constants.ureg.cubic_centimeter  # Volume of the entity in cubic centimeters
    def __init__(self, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        """Initialize the Entity."""
        super().__init__(*args, **kwargs)

