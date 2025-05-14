import random
from typing import List, Tuple
from player import Player


def olisort_challenge() -> Tuple[bool, str, str]:
    """
    Challenge: sort a list of random integers.

    Steps:
      1. Generate a random list of 10 ints between 0 and 100.
      2. Call Player.olisort to get the player's sorted list.
      3. Compute the expected sorted list using Python's sorted().
      4. Compare and return (passed, expected_str, actual_str).
    """
    # 1) generate input
    data: List[int] = [random.randint(0, 100) for _ in range(10)]

    # 2) get player's result via stub
    # We assume Player.olisort is implemented in player.py
    player = Player((0, 0), 0, 0)  # dummy position and bounds
    player_result: List[int] = player.olisort(data)

    # 3) expected result
    expected: List[int] = sorted(data)

    # 4) compare and return
    passed: bool = player_result == expected
    return passed, str(expected), str(player_result)
