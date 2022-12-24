# XXX: WTF Imaginary numbers? Use them next time

jets = open('input.txt').read().strip()
assert all(ch in '<>' for ch in jets)
jets = [(1, 0) if ch == '>' else (-1, 0) for ch in jets]


def rocks(i):
    r = [{(0, 0), (1, 0), (2, 0), (3, 0)},
         {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},
         {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
         {(0, 0), (0, 1), (0, 2), (0, 3)}, {(0, 0), (0, 1), (1, 0), (1, 1)}]
    return r[i % 5]


def hash(rock_idx, jet_idx):
    maxys = []
    for i in range(7):
        maxys.append((i, max([y for x, y in tower if y == i] + [0])))
    return (rock_idx % 5, jet_idx % len(jets), frozenset(maxys))


def valid(rock, jet, cur):
    rock_pos = set((cur[0] + x + jet[0], cur[1] + y + jet[1]) for x, y in rock)
    return all(rkx in range(7) and rky > 0 and (rkx, rky) not in tower
               for rkx, rky in rock_pos)
    # for rkx, rky in rock_pos:
    #     if rkx not in range(7):
    #         return False
    #     if rky <= 0:
    #         return False
    #     # collides with existing
    #     if (rkx, rky) in tower:
    #         return False
    # return True


top = 0
tower = set()
r_idx = 0
j_idx = 0
STEPS1 = 2022
STEPS2 = 1000000000000
cache = dict()

for r_idx in range(STEPS2):
    if r_idx == STEPS1:
        print(top)
    cur = (2, top + 4)

    cache_key = hash(r_idx, j_idx)
    if cache_key in cache and r_idx > STEPS1:
        step, T = cache[cache_key]
        div, mod = divmod(STEPS2 - r_idx, r_idx - step)
        # remaining steps to go to STEPS2 // steps per cycle = number of cycles
        # Instead of recognizing a cycle and go immediately,
        # we wait until the cycle gets to exactly STEPS2 steps
        # rather than some (STEPS2 - eps) for some eps
        if mod == 0:
            print(top + (top - T) * div)
            break
    else:
        cache[cache_key] = r_idx, top

    rock = rocks(r_idx)
    while True:
        jet = jets[j_idx % len(jets)]
        j_idx += 1
        if valid(rock, jet, cur):
            cur = (cur[0] + jet[0], cur[1] + jet[1])
        if valid(rock, (0, -1), cur):
            cur = (cur[0], cur[1] - 1)
        else:
            break
    tower |= {(cur[0] + x, cur[1] + y) for x, y in rock}
    top = max(top, cur[1] + max(y for _, y in rock))
