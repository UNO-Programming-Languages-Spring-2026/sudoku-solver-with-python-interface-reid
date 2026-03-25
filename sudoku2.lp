% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...
#const n = 9.
#const block = 3.
sudoku(X,Y,Z) :- initial(X,Y,Z).
% Achieved: All initial cells are loaded into the sudoku set

{ sudoku(X,Y,Z): Z = 1..n} = 1 :- X = 1..n, Y = 1..n.

:- sudoku(X1, Y1, Z1), sudoku(X2, Y2, Z2), X1 != X2, Y1 = Y2, Z1 = Z2.
%Achieved: Checks if there is a duplicate value on a given column and removes it

:- sudoku(X1, Y1, Z1), sudoku(X2, Y2, Z2), X1 = X2, Y1 != Y2, Z1 = Z2.
%Achieved: Checks if there is duplicate value on a given row and removes it

subgrid(X, Y, G) :- G = 1+( ((X-1)/block)*block + (Y-1)/block ), X = 1..n, Y = 1..n.

% Achieved: All cells are mapped to a single subgrid of size n

:- sudoku(X1, Y1, Z), sudoku(X2, Y2, Z), subgrid(X1, Y1, N), subgrid(X2, Y2, N), (X1, Y1) != (X2, Y2).

#show sudoku/3.
