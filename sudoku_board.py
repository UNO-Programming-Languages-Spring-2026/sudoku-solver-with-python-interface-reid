from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        block_size = 3
        for row in range(1,10):
            for col in range(1,10):
                if col % block_size == 0:
                    s += f'{self.sudoku[(row,col)]}  '
                else:
                    s += f'{self.sudoku[(row,col)]} '
            if row % block_size == 0:
                s += "\n\n"
            else:
                s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        board = model.symbols(shown=True)
        for cell in board:
            position = tuple((cell.arguments[0].number, cell.arguments[1].number))
            value = cell.arguments[2].number
            sudoku[position] = value
        return cls(sudoku)
