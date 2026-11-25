from typing import Self

from .objs import GameState, Mech, Map, Tile, TileType, random_state

# from .actions import ...


class GameEngine:
    def __init__(self, state: GameState) -> None:
        self._state = state

    @classmethod
    def init(cls) -> Self:
        return cls(random_state())
