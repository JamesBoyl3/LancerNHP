from dataclasses import dataclass


@dataclass
class GameState:
    mechs: list[Mech]
    map: Map


@dataclass
class Mech:
    pos: tuple[int, int]
    hp: int
    heat: int
    actions_left: int
    flying: bool = False


@dataclass
class Map:
    tiles: list[Tile]


@dataclass
class Tile:
    coords: tuple[int, int]
    type: TileType


@dataclass
class TileType:
    mov_mod: int = 0


def random_state(map_dims: tuple[int, int], no_mechs: tuple[int, int]) -> GameState:
    """
        Generates a random game state and returns it

        Args:
            no_mechs (tuple[int, int]): Number of mechs to deploy, in form (no_team1, no_team2)
        
        Returns:
            GameState: An object containing all relevant information for the current state of a game.

    """

    map = Map(
        [Tile(coords=(x, y)) for x in range(map_dims[0])] for y in range(map_dims[1])
    )
    mechs = [
            Mech(pos=(0,0), hp=1, heat=1, actions_left=1) for _ in range(no_mechs)
            ]

    return GameState(mechs=[Mech(pos=(1, 2), hp=1, heat=2, actions_left=2)], map=Map())
