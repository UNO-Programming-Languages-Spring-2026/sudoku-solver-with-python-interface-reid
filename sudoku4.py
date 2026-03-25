import clingo, sys
import sudoku_board

class ClingoApp(clingo.application.Application):
    
    def print_model(self, model, printer) -> None:
        boardStr = sudoku_board.Sudoku.from_model(model)
        print(boardStr)
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.load("sudoku2.lp")
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground([("base", [])])
        ctl.solve()


clingo.application.clingo_main(ClingoApp())