from pathlib import Path

from bingo import Cell, Board

root = Path(__file__).parent


with open(root/"input.txt") as input_file:
    lines = input_file.read().splitlines()
    raw_numbers, _, *raw_boards = lines
    boards = []
    single_board = []
    current_id = 1
    for row in raw_boards:
        if not row:
            boards.append(Board([Cell(v) for v in single_board], current_id))
            single_board = []
            current_id += 1
            continue
        single_board.extend(row.split())
    boards.append(Board([Cell(v) for v in single_board], current_id))

    for called_value in raw_numbers.split(","):
        final = None
        for board in boards:
            if board.check_call(called_value):
                final = sum(int(cell.value) for cell in board if not cell.covered) * int(called_value)
        if final is not None:
            break
    print(final)
