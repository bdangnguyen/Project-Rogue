import tcod.event

from typing import Optional
from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    """Handles all of the possible inputs that we currently care about.
    
    At the moment, we are just verifying that movement, and exiting the program
    works.
    """

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        """Overrides EventDispatch's ev_quit. Handles exiting the window.
        
        Args:
            self: Instance to the EventHandler. 
            event: The Quit event. Which occurs when we press "x".
        
        Raises:
            SystemExit(): Closes and cleans resources when we want to quit. 
        """

        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        """Overrides EventDispatch's ev_keydown. Handles keyboard actions.
        
        Args:
            self: Instance to the EventHandler.
            event: The KeyDown event. Which occurs when we press a key.
        
        Returns:
            action: The action associated with the key press.
        """

        action: Optional[Action] = None

        key = event.sym

        # Movement Handling. Note that the origin (1,1) is in the top left
        # of the screen. This implies that (mapWidth, mapHeight) is in the
        # bottom right of the screen. Moving up should decrease to 1, moving
        # down should increase to mapHeight, moving left should decrease to 1,
        # and moving right should increase to mapWidth.
        if key == tcod.event.K_UP:
            action = MovementAction(dx = 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx = 0, dy = 1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx = -1, dy = 0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx = 1, dy = 0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
