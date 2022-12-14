import json
import math
from functools import cmp_to_key
blocks = open("input.txt").read().split('\n\n')

ans1 = 0
pairs = []
for block in blocks:
    p1, p2 = block.strip().split('\n')
    pairs.append((json.loads(p1), json.loads(p2)))


def cmp(p1, p2):
    match p1, p2:
        case int(), int():
            if p1 < p2:
                return -1
            elif p1 == p2:
                return 0
            return 1
        case int(), list():
            return cmp([p1], p2)
        case list(), int():
            return cmp(p1, [p2])
        case list(), list():
            for i in range(len(p1)):
                if i >= len(p2):
                    return 1
                res = cmp(p1[i], p2[i])
                if res:
                    return res
            return cmp(len(p1), len(p2))



for i, (p1, p2) in enumerate(pairs):
    if cmp(p1, p2) == -1:
        ans1 += i + 1

print(ans1)
packets = sorted(sum(pairs, ([2], [6])), key=cmp_to_key(cmp))
print(math.prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]]))
