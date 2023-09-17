import CSP
import utils

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 0, 0]
          ]


# Variables
variables = [(i, j) for i in range(9) for j in range(9)]
# Domains
Domains = {var: set(range(1, 10)) if puzzle[var[0]][var[1]] == 0
           else {puzzle[var[0]][var[1]]} for var in variables}

# constraints
constraints = {}
for i in range(9):
    for j in range(9):
        utils.add_constraint(constraints, (i, j))

# Solution
print('*'*7, 'Solution', '*'*7)
csp = CSP.CSP(variables, Domains, constraints)
sol = csp.solve()

solution = [[0 for i in range(9)] for i in range(9)]
for i, j in sol:
    solution[i][j] = sol[i, j]

utils.print_sudoku(solution)
