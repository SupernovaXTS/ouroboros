"""Location for data imported from data."""
from __future__ import annotations

from types import SimpleNamespace

from ingest import Ingester

ingester = Ingester()

# Ego shit
chargen = ingester.ingestfile("chargen.json")

aptitudes = ingester.ingestfile("aptitudes.json")
aptitude_templates = ingester.ingestfile("aptitude_templates.json")
backgrounds = ingester.ingestfile("backgrounds.json")
careers = ingester.ingestfile("careers.json")
factions = ingester.ingestfile("factions.json")
interests = ingester.ingestfile("interests.json")
traits = ingester.ingestfile("traits.json")
reputations = ingester.ingestfile("reputations.json")
sleights = ingester.ingestfile("sleights.json")

# Morphs
morph_types = ingester.ingestfile("morph_types.json")
morphs = ingester.ingestfile("morphs.json")

# Gear and services
gear = SimpleNamespace()
gear.armor = ingester.ingestfile("gear_armor.json")
gear.bots = ingester.ingestfile("gear_bots.json")
gear.categories = ingester.ingestfile("gear_categories.json")
gear.comms = ingester.ingestfile("gear_comms.json")
gear.creatures = ingester.ingestfile("gear_creatures.json")
gear.drugs = ingester.ingestfile("gear_drugs.json")
gear.items = ingester.ingestfile("gear_items.json")
gear.mission = ingester.ingestfile("gear_mission.json")
gear.nano = ingester.ingestfile("gear_nano.json")
gear.packs = ingester.ingestfile("gear_packs.json")
gear.security = ingester.ingestfile("gear_security.json")
gear.software = ingester.ingestfile("gear_software.json")
gear.swarms = ingester.ingestfile("gear_swarms.json")
gear.vehicles = ingester.ingestfile("gear_ware.json")

services = ingester.ingestfile("services.json")

# Weapons
weapons = SimpleNamespace()

weapons.ammo = ingester.ingestfile("weapons_ammo.json")
weapons.melee = ingester.ingestfile("weapons_melee.json")
weapons.ranged = ingester.ingestfile("weapons_ranged.json")
