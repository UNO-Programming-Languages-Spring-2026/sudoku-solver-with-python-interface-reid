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
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        context = Context()
        ctl.ground(context=context)
        ctl.solve()


clingo.application.clingo_main(ClingoApp())