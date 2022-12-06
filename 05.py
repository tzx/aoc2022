import re
from collections import deque
block, lines = [blocks for blocks in open("input.txt").read().split('\n\n')]
lines = [line.strip() for line in lines.strip().split('\n')]
NUM = 9
crates = [deque() for _ in range(NUM)]
for line in block.split('\n')[:-1]:
    for i in range(NUM):
        char = line[i * 4 + 1]
        if char != " ":
            crates[i].append(char)
crates2 = [q.copy() for q in crates]

for line in lines:
    amt, fr, to = map(int, re.findall(r'\d+', line))
    buffer = []
    for i in range(amt):
        crates[to-1].appendleft(crates[fr-1].popleft())
        popped = crates2[fr-1].popleft()
        buffer.append(popped)
    crates2[to-1].extendleft(buffer[::-1])

print("".join(crate[0] for crate in crates))
print("".join(crate[0] for crate in crates2))
