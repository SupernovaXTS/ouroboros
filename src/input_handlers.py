from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

events = tcod.event.KeySym
MOVE_KEYS = {
    # Arrow keys.
    events.UP: (0, -1),
    events.DOWN: (0, 1),
    events.LEFT: (-1, 0),
    events.RIGHT: (1, 0),
    events.HOME: (-1, -1),
    events.END: (-1, 1),
    events.PAGEUP: (1, -1),
    events.PAGEDOWN: (1, 1),
    # Numpad keys.
    events.KP_1: (-1, 1),
    events.KP_2: (0, 1),
    events.KP_3: (1, 1),
    events.KP_4: (-1, 0),
    events.KP_6: (1, 0),
    events.KP_7: (-1, -1),
    events.KP_8: (0, -1),
    events.KP_9: (1, -1),
    # Vi keys.
    events.H: (-1, 0),
    events.J: (0, 1),
    events.K: (0, -1),
    events.L: (1, 0),
    events.Y: (-1, -1),
    events.U: (1, -1),
    events.B: (-1, 1),
    events.N: (1, 1),
}

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        if key == events.UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == events.DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == events.LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == events.RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action
