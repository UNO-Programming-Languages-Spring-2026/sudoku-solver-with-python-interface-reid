from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
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
