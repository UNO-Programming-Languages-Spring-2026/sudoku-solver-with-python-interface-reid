from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        block_size = 3
        #Iterate over each row and col
        for row in range(1,10):
            for col in range(1,10):

                #If the column size if a multiple of 3, then add an extra space
                if col % block_size == 0:
                    s += f'{self.sudoku[(row,col)]}  '
                else:
                    s += f'{self.sudoku[(row,col)]} '

            #If the row is a multiple of 3, add an extra newline
            if row % block_size == 0:
                s += "\n\n"
            else:
                s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        row = 1
        col = 1
        i = 0
        # Split list into individual parts
        newStr = s.split()
        #Iterate over each element
        while i < len(newStr):
            if col > 9:
                col = 1
                row += 1
            #calculate the position tuple
            position = (row, col)
            
            #If the value is a digit then add it to the sudoku board
            if newStr[i].isdigit():
                sudoku[position] = int(newStr[i])

            #Iterate to the next element
            i += 1
            col += 1

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        #Grab all symbols from the model
        board = model.symbols(shown=True)

        #Iterate over each
        for cell in board:
            #Find the position based on the first two arguments in the cell
            position = tuple((cell.arguments[0].number, cell.arguments[1].number))

            #Get the value as the next element
            value = cell.arguments[2].number

            #Add the pair into the dictionary
            sudoku[position] = value
        return cls(sudoku)
