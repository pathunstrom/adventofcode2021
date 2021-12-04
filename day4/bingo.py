from dataclasses import dataclass
from itertools import chain

from pytest import mark


@dataclass
class Cell:
    value: str
    covered: bool = False


@dataclass
class Board:
    cells: list[Cell]
    id: int

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        yield from self.cells

    def __hash__(self):
        return hash(id(self))

    @property
    def rows(self):
        return ([*self.cells[index:index + 5]] for index in range(0, 25, 5))

    @property
    def columns(self):
        return (
            [c for c in self.cells[initial:26:5]]
            for initial
            in range(5)
        )

    @property
    def diagonals(self):
        yield [cell for cell in self.cells[0:26:6]]
        yield [cell for cell in self.cells[4:21:4]]

    def wins(self):
        for line in chain(self.rows, self.columns, self.diagonals):
            if self.winning_row(line):
                return True
        return False

    def winning_row(self, values: list[Cell]):
        if len(values) != 5:
            return False
        return all(cell.covered for cell in values)

    def check_call(self, value):
        for cell in self:
            if cell.value == value:
                cell.covered = True
        return self.wins()

    def __str__(self):
        return "\n".join(
            " ".join(
                f"{cell.value.ljust(2)}{[' ', 'X'][cell.covered]}"
                for cell
                in row
            )
            for row
            in self.rows
        )


@mark.parametrize(
    "cells, expected",
    (
        ([Cell(str(x)) for x in range(1, 26)], False),
        ([Cell(str(x), True) for x in range(1, 6)] + [Cell(str(x)) for x in range(6, 26)], True),
        ([Cell(str(x), not bool((x-1) % 5)) for x in range(1, 26)], True),
        ([Cell(str(x), x in [1, 7, 13, 19, 25]) for x in range(1, 26)], True),
        ([Cell(str(x), x in [5, 9, 13, 17, 21]) for x in range(1, 26)], True)
    )
)
def test_board_wins(cells, expected):
    board = Board(cells)
    assert board.wins() == expected


def test_board_columns():
    board = Board([Cell(str(x)) for x in range(1, 26)])
    assert len(board) == 25
    assert list(board.columns) == [
        [Cell("1"), Cell("6"), Cell("11"), Cell("16"), Cell("21")],
        [Cell("2"), Cell("7"), Cell("12"), Cell("17"), Cell("22")],
        [Cell("3"), Cell("8"), Cell("13"), Cell("18"), Cell("23")],
        [Cell("4"), Cell("9"), Cell("14"), Cell("19"), Cell("24")],
        [Cell("5"), Cell("10"), Cell("15"), Cell("20"), Cell("25")]
    ]

