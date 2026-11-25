
from dataclasses import dataclass
from typing import Protocol

from .objs import GameState 

class Command(Protocol):
    def is_legal(self, state: GameState) -> bool: ...
    def execute(self, state: GameState) -> None: ...

@dataclass
class Move(Command):
    mech_id: int
    targ_tile: tuple[int, int]

    def is_legal(self, state: GameState) -> bool:
        mech = state.mechs[self.mech_id]

        return (
                mech.actions_left > 0 and
                self.targ_tile in state.reachable_tiles(self.mech_id)
                )
    
    def execute(self, state: GameState) -> None:
        if not self.is_legal(state):
            raise ValueError(f"Illegal move: {self}")
        
        mech = state.mechs[self.mech_id]

        mech.pos = self.targ_tile
        mech.actions_left -= 1

@dataclass
class Attack(Command):
    mech_id: int
    target_id:int

    def is_legal(self, state: GameState) -> bool:
        mech = state.mechs[self.mech_id]

        return (
                mech.actions_left > 0 and
                target_id in state.valid_targets(self.mech_id)
                )

    def execute(self, state: GameState) -> None:
        if not self.is_legal(state):
            raise ValueError(f"Illegal attack: {self}")

        mech = state.mechs[self.mech_id]
        target_mech = state.mechs[self.target_id]
        weapon = mech.active_weapon

        target_mech.hp -= weapon.dmg - target_mech.ap

@dataclass
class EndTurn(Command):
    mech_id: int

    def is_legal(self, state: GameState) -> bool:
        return True

    def execute(self, state: GameState) -> None:
        if not self.is_legal(state):
            raise ValueError(f"Cannot end turn {self}")

        state.end_turn(self.mech_id)
