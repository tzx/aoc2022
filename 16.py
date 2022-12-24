import functools
import itertools
import re
from collections import defaultdict

lines = [li.strip() for li in open("input.txt")]

valves = set()
flow = dict()
distance = defaultdict(lambda: float('inf'))
# 3 Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
for li in lines:
    valve, rate, dests = re.fullmatch(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)",
        li).groups()
    valves.add(valve)
    flow[valve] = int(rate)
    for u in dests.split(', '):
        distance[u, valve] = 1
        distance[valve, u] = 1

for k, i, j in itertools.product(valves, valves, valves):
    distance[i, j] = min(distance[i, j], distance[i, k] + distance[k, j])


@functools.cache
def rec(minutes, cur_valve, unopened, use_elephant=False):
    li = []
    for v in unopened:
        time_left = minutes - distance[cur_valve, v] - 1
        if distance[cur_valve, v] >= minutes:
            continue
        you = time_left * flow[v] + rec(time_left, v, unopened - {v},
                                        use_elephant)
        li.append(you)
    # start searching using the elephant for the rest, when that happens can't
    # use elephant again. We ask this at each level, obviously it's better to
    # start using the elephant when we run out of time
    elephant = rec(26, 'AA', unopened) if use_elephant else 0
    # if not li:
    #     return 0
    return max(li + [elephant])


print(rec(30, 'AA', frozenset(flow)))
print(rec(26, 'AA', frozenset(flow), True))
