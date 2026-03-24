from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        block_size = 3

        for row in range(1, 10):
            for col in range(1,10):
                # print(f"{(row, col)} - {self.sudoku[(row, col)]}")
                s += f"{self.sudoku[(row, col)]} "
                if col % block_size == 0:
                    s += " "
            s += "\n"
            if row % block_size == 0:
                s += "\n"

        # print(f"s:\n{s}")
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
        board = model.symbols(atoms=True)
        for cell in board:
            # print(cell.arguments) #

            position = tuple((cell.arguments[0].number, cell.arguments[1].number))
            value = cell.arguments[2].number

            # print(f"position={position} , value={value}")
            sudoku[position] = value

        # print(sudoku)
        return cls(sudoku)
