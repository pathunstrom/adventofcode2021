from operator import mul
from pathlib import Path

root = Path(__file__).parent

DEPTH = "depth"
HORIZONTAL = "horizontal"

position = {
    DEPTH: 0,
    HORIZONTAL: 0
}

translation = {
    "forward": (HORIZONTAL, 1),
    "up": (DEPTH, -1),
    "down": (DEPTH, 1)
}

with open(root/"input.txt") as input_file:
    for line in input_file:
        command, value = line.split()
        key, mod = translation[command]
        position[key] += int(value) * mod
    print(mul(*position.values()))
