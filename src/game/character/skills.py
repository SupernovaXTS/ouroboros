"""Skills module for character management."""
from __future__ import annotations

import fields
from ego import Aptitudes
from skill import SKILLRANGES, Skill, skillfield

athletics = Skill("Athletics", Aptitudes.reflexes, ["active", "physical"], SKILLRANGES.UNTRAINED.value)
deceive = Skill("Deceive", Aptitudes.savvy, ["active", "social"], SKILLRANGES.UNTRAINED.value)
fray = Skill("Fray", Aptitudes.reflexes, ["active", "combat"], SKILLRANGES.UNTRAINED.value)
freefall = Skill("Freefall", Aptitudes.somatics, ["active", "physical"], SKILLRANGES.UNTRAINED.value)
guns = Skill("Guns", Aptitudes.reflexes, ["active", "combat"], SKILLRANGES.UNTRAINED.value)
infiltrate = Skill("Infiltrate", Aptitudes.reflexes, ["active", "physical"], SKILLRANGES.UNTRAINED.value)
infosec = Skill("Infosec", Aptitudes.cognition, ["active", "technical"], SKILLRANGES.UNTRAINED.value)
interface = Skill("Interface", Aptitudes.cognition, ["active", "technical"], SKILLRANGES.UNTRAINED.value)
kinesics = Skill("Kinesics", Aptitudes.savvy, ["active", "social"], SKILLRANGES.UNTRAINED.value)
melee = Skill("Melee", Aptitudes.somatics, ["active", "combat"], SKILLRANGES.UNTRAINED.value)
perceive = Skill("Perceive", Aptitudes.intuition, ["active", "general"], SKILLRANGES.UNTRAINED.value)
persuade = Skill("Persuade", Aptitudes.savvy, ["active", "social"], SKILLRANGES.UNTRAINED.value)
program = Skill
# Base Skill Catchall for less common skills
base_exotic = Skill("Exotic", Aptitudes.cognition, ["active","field"], SKILLRANGES.UNTRAINED.value)

# Base Know Skills - Split into types due to the existence of fields
base_academics = Skill("Academics", Aptitudes.cognition, ["field","know"], SKILLRANGES.UNTRAINED.value)
base_arts = Skill("Arts", Aptitudes.intuition, ["field","know"], SKILLRANGES.UNTRAINED.value)
base_interests = Skill("Interests", Aptitudes.cognition, ["field","know"], SKILLRANGES.UNTRAINED.value)
base_profession = Skill("Profession", Aptitudes.cognition, ["field","know"], SKILLRANGES.UNTRAINED.value)
base_hardware = Skill("Hardware", Aptitudes.cognition, ["active","field", "technical"], SKILLRANGES.UNTRAINED.value)
base_medicine = Skill("Medicine", Aptitudes.cognition, ["active","field", "technical"], SKILLRANGES.UNTRAINED.value)
base_piloting = Skill("Pilot", Aptitudes.reflexes, ["active","field","technical"], SKILLRANGES.UNTRAINED.value)

academics = skillfield(base_academics, fields.academic)
arts = skillfield(base_arts, fields.arts)
interests = skillfield(base_interests, fields.interests)
profession = skillfield(base_profession, fields.profession)
hardware = skillfield(base_hardware, fields.hardware)
medicine = skillfield(base_medicine, fields.medicine)
piloting = skillfield(base_piloting, fields.pilot)
