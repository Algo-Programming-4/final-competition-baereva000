from typing import Tuple, List

Position = Tuple[int, int]

class Player:
    """
    Handles position and movement; student must implement olisort.
    """
    def __init__(self, start_pos: Position, rows: int, cols: int):
        self.pos = start_pos
        self.rows = rows
        self.cols = cols

    def get_position(self) -> Position:
        return self.pos

    def move(self, direction: str) -> None:
        r, c = self.pos
        if direction == 'up' and r > 0:
            r -= 1
        elif direction == 'down' and r < self.rows - 1:
            r += 1
        elif direction == 'left' and c > 0:
            c -= 1
        elif direction == 'right' and c < self.cols - 1:
            c += 1
        self.pos = (r, c)

    def olisort(self, data: List[int]) -> List[int]:
        """
        Student stub: sort data and return new list.
        """
        pass
