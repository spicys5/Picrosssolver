# <option value="10x10" selected="selected">10x10</option>
from Solver import Solver

html = input('Print the picross html here')

print(html)

row = [0] * 5
field = [row.copy()] * 5


s = Solver(field, 0, 0)
s.solveCross()