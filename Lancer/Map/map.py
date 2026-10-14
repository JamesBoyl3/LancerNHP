
from dataclasses import dataclass
from enum import Enums
from typing import Self

DIRECTIONS = [
		Hex(1,0), Hex(1, -1), Hex(-1, 1)
		Hex(-1, 0), Hex(0, -1), Hex(0, 1)
		]

class TileType(Enum):
	UNKOWN = 0
	FREE = 1
	BLOCKED = 2

@dataclass(frozen=True):
class HexTile:
	q: int
	r: int
	type: TileType

	@property
	def s(self) -> int:
		return -self.q - self.r

	def __add__(self, other: "Hex") -> "Hex":
		return Hex(self.q + other.q, self.r + other.r)

	def distance_to(self, other: "Hex") -> None:
		dq = self.q - other.q
		dr = self.r - other.r
		ds = self.s - other.s
		return max(abs(dq), abs(dr), abs(ds))

	def neighbors(self) -> list["Hex"]:
		return [self + d for d in DIRECTIONS]

	def within_range(self, n: int) -> list["Hex"]:
		results = []
		for dq in range(-n, n + 1):
			for dr in range(max(-n, -dq - n), min(n, -dq + n) + 1):
				results.append(Hex(self.q + dq, self.r + dr))
		return results

@dataclass(frozen=True)
Class Map:
	self.tiles: list[HexTile]

	def generate_map(self) -> Self:
		tiles = []
		return Map(tiles)
