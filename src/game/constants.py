from __future__ import annotations  # noqa: D100

import mcrfpy  # pyright: ignore[reportMissingModuleSource]
import pint

ureg = pint.UnitRegistry()
# Sprite indices for CP437 tileset
SPRITE_WALL = 35    # '#' - wall
SPRITE_FLOOR = 46   # '.' - floor
SPRITE_PLAYER = 64  # '@' - player
SPRITE_CORPSE = 37  # '%' - remains
SPRITE_POTION = 173 # Potion sprite
SPRITE_CURSOR = 88  # 'X' - targeting cursor
SPRITE_STAIRS_DOWN = 62  # '>' - stairs down
SPRITE_SWORD = 47   # '/' - weapon
SPRITE_ARMOR = 91   # '[' - armor

# Enemy sprites
SPRITE_GOBLIN = 103  # 'g'
SPRITE_ORC = 111     # 'o'
SPRITE_TROLL = 116   # 't'

# Grid dimensions
GRID_WIDTH = 50
GRID_HEIGHT = 30

# Room generation parameters
ROOM_MIN_SIZE = 6
ROOM_MAX_SIZE = 12
MAX_ROOMS = 8

# FOV and targeting settings
FOV_RADIUS = 8
RANGED_ATTACK_RANGE = 6
RANGED_ATTACK_DAMAGE = 4

# Save file location
SAVE_FILE = "savegame.json"

# XP values for enemies
ENEMY_XP_VALUES = {
    "goblin": 35,
    "orc": 50,
    "troll": 100
}

# Visibility colors
COLOR_VISIBLE = mcrfpy.Color(0, 0, 0, 0)
COLOR_DISCOVERED = mcrfpy.Color(0, 0, 40, 180)
COLOR_UNKNOWN = mcrfpy.Color(0, 0, 0, 255)

# Message colors
COLOR_PLAYER_ATTACK = mcrfpy.Color(200, 200, 200)
COLOR_ENEMY_ATTACK = mcrfpy.Color(255, 150, 150)
COLOR_PLAYER_DEATH = mcrfpy.Color(255, 50, 50)
COLOR_ENEMY_DEATH = mcrfpy.Color(100, 255, 100)
COLOR_HEAL = mcrfpy.Color(100, 255, 100)
COLOR_PICKUP = mcrfpy.Color(100, 200, 255)
COLOR_INFO = mcrfpy.Color(100, 100, 255)
COLOR_WARNING = mcrfpy.Color(255, 200, 50)
COLOR_INVALID = mcrfpy.Color(255, 100, 100)
COLOR_RANGED = mcrfpy.Color(255, 255, 100)
COLOR_SAVE = mcrfpy.Color(100, 255, 200)
COLOR_DESCEND = mcrfpy.Color(200, 200, 255)
COLOR_LEVEL_UP = mcrfpy.Color(255, 255, 100)
COLOR_XP = mcrfpy.Color(200, 200, 100)
COLOR_EQUIP = mcrfpy.Color(150, 200, 255)

# UI Layout constants
UI_TOP_HEIGHT = 60
UI_BOTTOM_HEIGHT = 150
GAME_AREA_Y = UI_TOP_HEIGHT
GAME_AREA_HEIGHT = 768 - UI_TOP_HEIGHT - UI_BOTTOM_HEIGHT
