import re
from copy import deepcopy

lines = [li.strip() for li in open("input.txt")]

cave = {}
for li in lines:
    parts = re.findall(r"(\d+),(\d+)", li)
    for idx in range(len(parts) - 1):
        sx, sy, ex, ey = map(int, (*parts[idx], *parts[idx + 1]))
        dx, dy = ex - sx, ey - sy
        cave[sx, sy] = '#'
        for i in range(max(abs(dx), abs(dy)) + 1):
            x = sx + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
            y = sy + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
            cave[x, y] = '#'
cave_copy = deepcopy(cave)

SANDX, SANDY = 500, 0
deepest = max(y for x, y in cave.keys())


def drop(deepest):
    x, y = SANDX, SANDY
    while (x, y) not in cave:
        if y > deepest:
            return False
        if (x, y + 1) not in cave:
            y += 1
            continue
        if (x - 1, y + 1) not in cave:
            x -= 1
            y += 1
            continue
        elif (x + 1, y + 1) not in cave:
            x += 1
            y += 1
            continue
        cave[x, y] = "o"
        return True


ans1 = 0
while drop(deepest):
    ans1 += 1
print(ans1)

floor = deepest + 2
cave = cave_copy
for i in range(
        min(x for x, _ in cave.keys()) - 2000,
        max(x for x, _ in cave.keys()) + 2000):
    cave[i, floor] = "#"

ans2 = 0
while cave.get((500, 0)) is None:
    assert drop(floor)
    ans2 += 1
print(ans2)
