import clingo, sys
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []
        for (row, col), value in self.board.sudoku.items():
            symbol = clingo.Function( "",[clingo.Number(row), clingo.Number(col), clingo.Number(value)])
            symbols.append(symbol)
        return symbols

class ClingoApp(clingo.application.Application):
    
    def print_model(self, model, printer) -> None:
        boardStr = Sudoku.from_model(model)
        print(boardStr)
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.load("sudoku2.lp")
        ctl.load("sudoku_py.lp")

        if files:
            with open(files[0], "r") as f:
                board_str = f.read()
        else:
            board_str = sys.stdin.read()
            
        board = Sudoku.from_str(board_str)
        context = Context(board)
        ctl.ground([("base", [])], context=context)
        ctl.solve()


clingo.application.clingo_main(ClingoApp())