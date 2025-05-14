import random
from typing import List, Tuple, Set, Dict

# Type aliases
Grid = List[List[str]]
Position = Tuple[int, int]

# Import challenge implementations
from challenges import olisort_challenge


def create_room(rows: int, cols: int, num_challenges: int) -> Tuple[Grid, Position, List[Position]]:
    """
    Creates a rectangular grid (room) with:
      - one starting tile marked 'S'
      - num_challenges challenge tiles marked 'C'
      - all other tiles as '.'

    Returns:
      grid: 2D list of tile characters
      start_pos: (row, col) of the start location
      challenge_positions: list of (row, col) for each challenge
    """
    grid: Grid = [['.' for _ in range(cols)] for _ in range(rows)]
    start_row = random.randrange(rows)
    start_col = random.randrange(cols)
    grid[start_row][start_col] = 'S'
    start_pos: Position = (start_row, start_col)

    challenge_positions: Set[Position] = set()
    while len(challenge_positions) < num_challenges:
        r = random.randrange(rows)
        c = random.randrange(cols)
        if grid[r][c] == '.':
            grid[r][c] = 'C'
            challenge_positions.add((r, c))

    return grid, start_pos, list(challenge_positions)


def print_room(grid: Grid) -> None:
    """
    Prints the grid in ASCII form. Example:
      . . C .
      . S . .
    """
    for row in grid:
        print(' '.join(row))


class Player:
    """
    Default player with position tracking and simple movement.
    """
    def __init__(self, start_pos: Position, rows: int, cols: int):
        self.pos: Position = start_pos
        self.rows = rows
        self.cols = cols

    def get_position(self) -> Position:
        return self.pos

    def move(self, direction: str) -> None:
        row, col = self.pos
        if direction == 'up' and row > 0:
            row -= 1
        elif direction == 'down' and row < self.rows - 1:
            row += 1
        elif direction == 'left' and col > 0:
            col -= 1
        elif direction == 'right' and col < self.cols - 1:
            col += 1
        self.pos = (row, col)


if __name__ == "__main__":
    # Configuration
    ROWS, COLS = 6, 10
    NUM_CHALLENGES = 4

    # Create room and player
    grid, start, challenges = create_room(ROWS, COLS, NUM_CHALLENGES)
    player = Player(start, ROWS, COLS)

    # Map each challenge position to its function (for now, all sort)
    challenge_map: Dict[Position, callable] = {pos: olisort_challenge for pos in challenges}

    # Display initial room
    print_room(grid)
    print(f"Player starts at {player.get_position()}")
    print(f"Challenges at {challenges}\n")

    directions = ['up', 'right', 'down', 'left']
    deltas = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

    moves = 0
    found: Set[Position] = set()
    current_dir = random.choice(directions)
    turn_chance = 0.2

    # Scoring
    challenge_points = 0

    # Phase 1: find and run all challenges
    while len(found) < NUM_CHALLENGES:
        row, col = player.get_position()
        dr, dc = deltas[current_dir]
        nr, nc = row + dr, col + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            player.move(current_dir)
            moves += 1
            if random.random() < turn_chance:
                idx = directions.index(current_dir)
                current_dir = directions[(idx + random.choice([-1,1])) % len(directions)]
            pos = player.get_position()
            if pos in challenges and pos not in found:
                found.add(pos)
                # activate challenge
                passed, expected, actual = challenge_map[pos]()
                pts = 15 if passed else 0
                challenge_points += pts
                print(f"Challenge at {pos}: passed={passed}, expected={expected}, actual={actual} -> +{pts} points")
        else:
            idx = directions.index(current_dir)
            current_dir = directions[(idx + random.choice([-1,1])) % len(directions)]

    # Phase 2: return home
    while player.get_position() != start:
        row, col = player.get_position()
        dr, dc = deltas[current_dir]
        nr, nc = row + dr, col + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            player.move(current_dir)
            moves += 1
            if random.random() < turn_chance:
                idx = directions.index(current_dir)
                current_dir = directions[(idx + random.choice([-1,1])) % len(directions)]
        else:
            idx = directions.index(current_dir)
            current_dir = directions[(idx + random.choice([-1,1])) % len(directions)]

    move_penalty = moves
    total_score = challenge_points - move_penalty

    print(f"Returned home at {player.get_position()} after {moves} total moves")
    print(f"Challenge points: {challenge_points}")
    print(f"Move penalties: {move_penalty}")
    print(f"Total score: {total_score}")
