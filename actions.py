# Base Action class to inherit from
class Action:
    pass

# EscapeAction class. At the moment, only used for easy exit.
class EscapeAction(Action):
    pass

# MovementAction class. At the moment, passes movement deltas to draw.
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy