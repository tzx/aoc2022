from collections import deque, defaultdict

board = [list(li) for li in [li.strip() for li in open('input.txt')]]
m, n = len(board), len(board[0])
SR, SC = [(r, c) for r in range(m) for c in range(n) if board[r][c] == 'S'][0]
ER, EC = [(r, c) for r in range(m) for c in range(n) if board[r][c] == 'E'][0]
board[SR][SC] = 'a'
board[ER][EC] = 'z'
STARTS1 = [(SR, SC)]
STARTS2 = [(r, c) for r in range(m) for c in range(n) if board[r][c] == 'a']

for starts in [STARTS1, STARTS2]:
    q = deque(starts)
    distance = defaultdict(lambda: float('inf'))
    for r, c in starts:
        distance[(r, c)] = 0
    while q:
        r, c = q.popleft()
        if (r, c) == (ER, EC):
            print(distance[(r, c)])
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dx, c + dy
            if nr in range(m) and nc in range(
                    n) and ord(board[nr][nc]) - ord(board[r][c]) <= 1:
                dist_to = distance[(r, c)] + 1
                if dist_to < distance[(nr, nc)]:
                    q.append((nr, nc))
                    distance[(nr, nc)] = dist_to
