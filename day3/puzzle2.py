from collections import Counter
from pathlib import Path

root = Path(__file__).parent

with open(root/"input.txt") as input_file:
    input_values = [list(line) for line in input_file.read().splitlines()]


def oxygen_generator_finder(values, index=0):
    most, least = Counter(v[index] for v in values).most_common()
    if most[1] == least[1]:
        keep = "1"
    else:
        keep = most[0]
    values = [v for v in values if v[index] == keep]
    if len(values) == 1:
        return int("".join(values[0]), 2)
    return oxygen_generator_finder(values, index + 1)


def carbon_dioxide_scrubber_finder(values, index=0):
    most, least = Counter(v[index] for v in values).most_common()
    if most[1] == least[1]:
        keep = "0"
    else:
        keep = least[0]
    values = [v for v in values if v[index] == keep]
    if len(values) == 1:
        return int("".join(values[0]), 2)
    return carbon_dioxide_scrubber_finder(values, index + 1)


print(oxygen_generator_finder(input_values) * carbon_dioxide_scrubber_finder(input_values))