import re
lines = [li.strip() for li in open('input.txt')]

# XXX: I forgor numpy
tup_add = lambda x, y: tuple(a + b for a, b in zip(x, y))
tup_sub = lambda x, y: tuple(a - b for a, b in zip(x, y))


def prune(reso_to_prod):
    PRUNE_NUM = 10000
    return sorted(reso_to_prod,
                  key=lambda x: tup_add(x[0], x[1]),
                  reverse=True)[:PRUNE_NUM]


def produce(cost_to_prod, time):
    # [(current resources, current production)]
    q = [((0, 0, 0, 0), (0, 0, 0, 1))]
    for _ in range(time):
        new = []
        for cur_resources, cur_prod in q:
            for cost, prod in cost_to_prod:
                if any(a < b for a, b in zip(cur_resources, cost)):
                    continue
                new_reso = tup_add(tup_sub(cur_resources, cost), cur_prod)
                new_prod = tup_add(cur_prod, prod)
                new.append((new_reso, new_prod))
        q = prune(new)
    return max(reso[0] for reso, _ in q)


ans1 = 0
ans2 = 1
for li in lines:
    id, i, ii, iii, iv, v, vi = map(int, re.findall(r"\d+", li))
    # costs from most valuable to least (geo, obs, clay, ore) to robot produce
    orc = ((0, 0, 0, i), (0, 0, 0, 1))
    clc = ((0, 0, 0, ii), (0, 0, 1, 0))
    obc = ((0, 0, iv, iii), (0, 1, 0, 0))
    gec = ((0, vi, 0, v), (1, 0, 0, 0))
    nothing = ((0, 0, 0, 0), (0, 0, 0, 0))
    ans1 += id * produce([orc, clc, obc, gec, nothing], 24)
    ans2 *= produce([orc, clc, obc, gec, nothing], 32) if id <= 3 else 1

print(ans1)
print(ans2)
