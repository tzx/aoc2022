lines = [(a, int(b))
         for a, b in [li.strip().split() for li in open("input.txt")]]
dir_tup = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}


def move(head, tail):
    headx, heady = head
    tailx, taily = tail
    if abs(headx - tailx) > 1 or abs(heady - taily) > 1:
        if abs(headx - tailx) > 0:
            tailx += 1 if headx > tailx else -1
        if abs(heady - taily) > 0:
            taily += 1 if heady > taily else -1
    return (tailx, taily)


visited = [{(0, 0)}, {(0, 0)}]
knots = [(0, 0) for _ in range(10)]
for dir_, amt in lines:
    dx, dy = dir_tup[dir_]
    for _ in range(amt):
        knots[0] = knots[0][0] + dx, knots[0][1] + dy
        for i in range(1, 10):
            knots[i] = move(knots[i - 1], knots[i])
        visited[0].add(knots[1])
        visited[1].add(knots[9])

print(len(visited[0]))
print(len(visited[1]))
