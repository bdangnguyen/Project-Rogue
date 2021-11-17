import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    # Create a new tcod contex. Specifically a context window with
    # desired size and tileset.
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Project Rogue",
        vsync=True,
    ) as context:
        # This creates a new console with coordinate system (x,y) instead of
        # the default (y,x).
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")
            
            # This "draws" the console.
            context.present(root_console)

            # This "clears" the console. Combine above and you get a frame
            # rendering call.
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()