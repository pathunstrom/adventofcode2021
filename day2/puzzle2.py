from pathlib import Path

root = Path(__file__).parent

aim = 0
position = 0
depth = 0

aim_commands = {"up": -1, "down": 1}

with open(root/"input.txt") as input_file:
    for line in input_file:
        command, input_value = line.split()
        value = int(input_value)
        if command in aim_commands:
            aim += value * aim_commands[command]
        else:
            position += value
            depth += value * aim
    print(position * depth)
