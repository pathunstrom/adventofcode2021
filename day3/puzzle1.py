from collections import Counter
from pathlib import Path

root = Path(__file__).parent

gamma = []
epsilon = []

with open(root/"input.txt") as input_file:
    for values in zip(*input_file.read().splitlines()):
        most, least = [x[0] for x in Counter(values).most_common()]
        gamma.append(most)
        epsilon.append(least)
print(int("".join(gamma), 2) * int("".join(epsilon), 2))
