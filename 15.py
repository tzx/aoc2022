import re
from collections import defaultdict
lines = [
    list(map(int, re.findall(r"-?\d+", li)))
    for li in [li.strip() for li in open('input.txt')]
]
board = defaultdict(lambda: '.')
Y = 2000000
for sx, sy, bx, by in lines:
    board[sx, sy] = 'S'
    board[bx, by] = 'B'
    dist = abs(sx - bx) + abs(sy - by)
    if Y in range(sy - dist, sy + dist + 1):
        diff = abs(Y - sy)
        for i in range(sx + diff - dist, sx - diff + dist + 1):
            if board[i, Y] != 'B':
                board[i, Y] = '#'
print(sum(1 for c, v in board.items() if v == '#' and c[1] == Y))

import z3
MAXY = 4000000
sat = z3.Solver()
x, y = z3.Int("x"), z3.Int("y")
sat.add(x >= 0)
sat.add(y >= 0)
sat.add(x <= MAXY)
sat.add(y <= MAXY)

# https://stackoverflow.com/questions/22547988/how-to-calculate-absolute-value-in-z3-or-z3py
z3abs = lambda x: z3.If(x > 0, x, -x)
for sx, sy, bx, by in lines:
    dist = abs(sx - bx) + abs(sy - by)
    sat.add(z3abs(sx - x) + z3abs(sy - y) > dist)
print(sat.check())
model = sat.model()
print(model[x].as_long() * MAXY + model[y].as_long())
