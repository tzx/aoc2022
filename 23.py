from collections import Counter

board = [list(line.strip()) for line in open('input.txt')]
elves = {x + 1j * y for y, row in enumerate(board) for x, cell in enumerate(row) if cell == '#'}
adj = [1, 1+1j, 1j, 1j-1, -1, -1-1j, -1j, 1-1j]
dirs = [-1j, 1j, -1, 1]

i = 0
old_elves = {}
while old_elves != elves:
    if i == 10:
        rs = [e.real for e in elves]
        cs = [e.imag for e in elves]
        print((max(rs) - min(rs) + 1) * (max(cs) - min(cs) + 1) - len(elves))
    old_elves = elves

    proposed = {e: e for e in elves}
    for elf in elves:
        neighbors = elves & {elf + adjjj for adjjj in adj}
        if not neighbors:
            continue
        for dirs_idx in range(i, i + 4):
            _dirs_idx = (dirs_idx) % 4
            d = dirs[_dirs_idx]
            adjj = elves & {elf + d, elf + d + d * 1j, elf + d - d * 1j}
            if not adjj:
                proposed[elf] = elf + d
                break
    proposed_cnt = Counter(proposed.values())
    canmove = {e for e in proposed if proposed_cnt[proposed[e]] == 1}
    cantmove = elves - canmove
    elves = cantmove | {proposed[e] for e in canmove}
    i += 1

print(i)
