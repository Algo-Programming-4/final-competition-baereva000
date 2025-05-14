[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/6B3OHK5d)
# Simulation Competition Repository

Welcome to the Simulation Competition! In this project, you will:

1. **Implement a challenge** in `challenges.py` based on an algorithm or data structure we’ve covered this year.
2. **Add a solution stub** in `player.py` (your method) that the simulation will call.
3. **Run** `simulation.py` to see your challenge in action in a text-based grid simulation.

---

## Repository Structure

```
competition/
├── player.py       # Player class and method stubs
├── challenges.py   # One file per challenge function
└── simulation.py   # Text-based simulation runner
```

* **player.py**: Contains the `Player` class (position, movement). Add your algorithm implementation here as a method stub.
* **challenges.py**: Define one function per challenge. Each generates its own test input, calls your player method, and returns `(passed, expected_str, actual_str)`.
* **simulation.py**: Sets up a rectangular grid, places the player and challenge tiles, and drives a simple wandering AI that invokes each challenge when landed on.

---

## Prerequisites

* Python 3.8 or higher

---

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd competition
   ```

2. **Implement your player method** in `player.py`:

   ```python
   from typing import Tuple, List

   class Player:
       def __init__(self, start_pos: Tuple[int,int], rows: int, cols: int):
           # existing code...
           pass

       # Example stub for a sorting challenge
       def olisort(self, data: List[int]) -> List[int]:
           """
           TODO: Implement your sorting algorithm here.
           :param data: list of integers to sort
           :return: new sorted list
           """
           raise NotImplementedError("Implement olisort in player.py")
   ```

3. **Add your challenge function** in `challenges.py`:

   ```python
   import random
   from typing import List, Tuple
   from player import Player

   def olisort_challenge() -> Tuple[bool, str, str]:
       """
       Sort Challenge:
       1) Generate list of 10 random ints [0-100]
       2) Call Player.olisort(data)
       3) Compare to sorted(data)
       4) Return (passed, expected_str, actual_str)
       """
       data: List[int] = [random.randint(0,100) for _ in range(10)]
       player = Player((0,0), 0, 0)  # dummy bounds
       result = player.olisort(data)
       expected = sorted(data)
       passed = (result == expected)
       return passed, str(expected), str(result)
   ```

   > **Tip:** Replace `olisort_challenge` and `olisort` with your own challenge name and method.

4. **Run the simulation**:

   ```bash
   python simulation.py
   ```

   The sim will:

   * Create a grid of size (configurable in `simulation.py`).
   * Wander the player until it lands on each challenge tile.
   * Invoke your challenge function and print the outcome and score.

---

## Configuration

In `simulation.py`, you can adjust:

* `ROWS`, `COLS`: grid dimensions
* `NUM_CHALLENGES`: how many tiles/challenges
* `POINTS_PER_CHALLENGE`: score awarded on pass
* Movement behavior parameters (turn chance, etc.)

---

## How to Submit

1. Commit all your changes: your implemented stubs and new challenges.
2. Push to your GitHub repo.
3. Submit the repo link on Canvas.

Good luck, and have fun designing those challenges! Feel free to ask questions if anything is unclear.
