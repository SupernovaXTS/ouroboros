"""Skills module for character management."""
from __future__ import annotations

import fields
from ego import Aptitudes
from skill import SKILLRANGES, Skill, skillfield

athletics = Skill("Athletics", Aptitudes.reflexes, ["active", "physical"], SKILLRANGES.UNTRAINED)
deceive = Skill("Deceive", Aptitudes.savvy, ["active", "social"], SKILLRANGES.UNTRAINED)
fray = Skill("Fray", Aptitudes.reflexes, ["active", "combat"], SKILLRANGES.UNTRAINED)
freefall = Skill("Freefall", Aptitudes.somatics, ["active", "physical"], SKILLRANGES.UNTRAINED)
guns = Skill("Guns", Aptitudes.reflexes, ["active", "combat"], SKILLRANGES.UNTRAINED)
infiltrate = Skill("Infiltrate", Aptitudes.reflexes, ["active", "physical"], SKILLRANGES.UNTRAINED)
infosec = Skill("Infosec", Aptitudes.cognition, ["active", "technical"], SKILLRANGES.UNTRAINED)
interface = Skill("Interface", Aptitudes.cognition, ["active", "technical"], SKILLRANGES.UNTRAINED)
kinesics = Skill("Kinesics", Aptitudes.savvy, ["active", "social"], SKILLRANGES.UNTRAINED)
melee = Skill("Melee", Aptitudes.somatics, ["active", "combat"], SKILLRANGES.UNTRAINED)
perceive = Skill("Perceive", Aptitudes.intuition, ["active", "general"], SKILLRANGES.UNTRAINED)
persuade = Skill("Persuade", Aptitudes.savvy, ["active", "social"], SKILLRANGES.UNTRAINED)
program = Skill("Program",Aptitudes.cognition, ["active","technical"], SKILLRANGES.UNTRAINED)
provoke = Skill("Provoke",Aptitudes.savvy, ["active","social"],SKILLRANGES.UNTRAINED)
psi = Skill("Psi",Aptitudes.willpower,["active","mental","psi"],SKILLRANGES.UNTRAINED)
research = Skill("Research",Aptitudes.intuition,["active","technical"],SKILLRANGES.UNTRAINED)
survival = Skill("Survival",Aptitudes.intuition,["active","mental"],SKILLRANGES.UNTRAINED)

# Base Skill Catchall for less common skills
base_exotic = Skill("Exotic", Aptitudes.cognition, ["active","field"], SKILLRANGES.UNTRAINED)

# Base Know Skills - Split into types due to the existence of fields
base_know = Skill("Know",Aptitudes.cognition,["Field","Know"],SKILLRANGES.UNTRAINED)
base_academics = Skill("Academics", Aptitudes.cognition, ["field","know"], SKILLRANGES.UNTRAINED)
base_arts = Skill("Arts", Aptitudes.intuition, ["field","know"], SKILLRANGES.UNTRAINED)
base_interests = Skill("Interests", Aptitudes.cognition, ["field","know"], SKILLRANGES.UNTRAINED)
base_profession = Skill("Profession", Aptitudes.cognition, ["field","know"], SKILLRANGES.UNTRAINED)
base_hardware = Skill("Hardware", Aptitudes.cognition, ["active","field", "technical"], SKILLRANGES.UNTRAINED)
base_medicine = Skill("Medicine", Aptitudes.cognition, ["active","field", "technical"], SKILLRANGES.UNTRAINED)
base_piloting = Skill("Pilot", Aptitudes.reflexes, ["active","field","technical"], SKILLRANGES.UNTRAINED)

academics = skillfield(base_academics, fields.academic)
arts = skillfield(base_arts, fields.arts)
interests = skillfield(base_interests, fields.interests)
profession = skillfield(base_profession, fields.profession)
hardware = skillfield(base_hardware, fields.hardware)
medicine = skillfield(base_medicine, fields.medicine)
piloting = skillfield(base_piloting, fields.pilot)

print(piloting.ground)
