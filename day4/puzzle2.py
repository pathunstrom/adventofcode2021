from collections import deque
from pathlib import Path
from pprint import pprint

from bingo import Cell, Board

root = Path(__file__).parent


def winnow(boards: list[Board], moves: deque[str]):
    move = moves.popleft()
    if len(boards) == 1:
        if boards[0].check_call(move):
            return boards[0], move
        else:
            return winnow(boards, moves)
    for board in boards:
        board.check_call(move)
    return winnow([board for board in boards if not board.wins()], moves)


with open(root/"input.txt") as input_file:
    lines = input_file.read().splitlines()
    raw_numbers, _, *raw_boards = lines
    boards = []
    single_board = []
    current_id = 1
    for row in raw_boards:
        if not row:
            board = Board([Cell(v) for v in single_board], current_id)
            assert len(board) == 25
            boards.append(board)
            single_board = []
            current_id += 1
            continue
        single_board.extend(row.split())
    boards.append(Board([Cell(v) for v in single_board], current_id))
    assert len(boards[-1]) == 25

    final_board, final_move = winnow(boards, deque(raw_numbers.split(",")))
    uncovered_total = sum(int(cell.value) for cell in final_board if not cell.covered)
    print(uncovered_total * int(final_move))

# Wrong: 9280
