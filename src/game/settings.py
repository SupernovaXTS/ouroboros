"""Settings for the game."""
from __future__ import annotations

import attrs


@attrs.define
class GameSettings:
    """Class for game settings."""
    weight_unit: str = "grams"  # Unit for weight measurements
    dimensions_unit: str = "centimeters"  # Unit for dimensions measurements (length, width, depth)
    speed_unit: str = "meters_per_second"  # Unit for speed measurements
    volume_unit: str = "cubic_centimeters"  # Unit for volume measurements
    sound_volume: float = 1.0  # Volume for sound effects (0.0 to 1.0)
    music_volume: float = 1.0  # Volume for music (0.0 to 1.0)
    fullscreen: bool = False   # Fullscreen mode
    resolution_width: int = 800  # Screen width in pixels
    resolution_height: int = 600  # Screen height in pixels
    show_fps: bool = False     # Show frames per second

