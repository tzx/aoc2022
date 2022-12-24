from collections import deque

lines = [
    tuple(map(int, li.split(',')))
    for li in [li.strip() for li in open("input.txt")]
]
max_c = max(max(lines, key=lambda x: max(x)))


def new_coords(x, y, z):
    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
                       (0, 0, -1)]:
        yield (x + dx, y + dy, z + dz)


ans = 0
for x, y, z in lines:
    for nx, ny, nz in new_coords(x, y, z):
        if (nx, ny, nz) not in lines:
            ans += 1
print(ans)

outer = set()
q = deque([(-1, -1, -1)])
while q:
    x, y, z = q.popleft()
    for nx, ny, nz in new_coords(x, y, z):
        if all(p in range(-1, max_c + 2) for p in [nx, ny, nz]) and (
                nx, ny, nz) not in outer and (nx, ny, nz) not in lines:
            q.append((nx, ny, nz))
            outer.add((nx, ny, nz))

ans2 = 0
for x, y, z in lines:
    for nx, ny, nz in new_coords(x, y, z):
        if (nx, ny, nz) in outer:
            ans2 += 1
print(ans2)
