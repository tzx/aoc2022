board = [list(li.strip()) for li in open('input.txt')]
M, N = len(board) - 2, len(board[0]) - 2


def wrap(num):
    return complex(num.real % N, num.imag % M)


dirs = {'x': 0, '<': -1, '>': 1, '^': -1j, 'v': 1j}
blz = {
    d: {
        complex(c, r)
        for c in range(N) for r in range(M) if board[r + 1][c + 1] == d
    }
    for d in dirs
}

start, end = 0 - 1j, N - 1 + M * 1j
print(start, end)
q, step, trip = [start], 0, 0
while q:
    blz = {d: {wrap(old + dirs[d]) for old in blz[d]} for d in dirs}
    step += 1
    to_visit = {nodes + dirs[d] for nodes in q for d in dirs}
    q = []
    for new in to_visit:
        if (trip, new) in ((0, end), (1, start), (2, end)):
            if trip == 0:
                print(step)
            if trip == 2:
                print(step)
                q = []
                break
            q, trip = [new], trip + 1
            break

        if all((new not in blz[d] for d in blz)) \
                and new == wrap(new) or new in (start, end):
            q += [new]
