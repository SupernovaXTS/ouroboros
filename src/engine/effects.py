"""A collection of effects."""

from __future__ import annotations

import attrs
from tcod.ecs import Entity  # noqa: TC002

from engine.combat import heal
from engine.components import Name
from engine.messages import add_message


@attrs.define
class Healing:
    """Healing effect."""

    amount: int

    def affect(self, entity: Entity) -> None:
        """Heal the target."""
        if amount := heal(entity, self.amount):
            add_message(
                entity.registry, f"""{entity.components.get(Name, "?")} recovers {amount} HP.""", fg="health_recovered"
            )
