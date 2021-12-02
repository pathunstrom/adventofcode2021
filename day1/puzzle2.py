from pathlib import Path

root = Path(__file__).parent

with open(root/"input.txt") as input_file:
    values = [int(line) for line in input_file]
    sliding_window = [sum(t) for t in zip(values, values[1:], values[2:])]
    print(sum(1 if this > last else 0 for last, this in zip(sliding_window, sliding_window[1:])))
