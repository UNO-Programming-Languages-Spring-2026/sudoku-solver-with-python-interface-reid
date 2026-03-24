import clingo

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku2.lp")
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground([("base", [])])
        ctl.solve()


clingo.application.clingo_main(ClingoApp())