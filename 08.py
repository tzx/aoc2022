import math
board = [list(map(int, list(li.strip()))) for li in open("input.txt")]

ans1 = 0
ans2 = 0
for r, row in enumerate(board):
    for c, cell in enumerate(row):
        scores = []
        vis = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            score = 1
            x, y = r + dx, c + dy
            while x in range(len(board)) and y in range(len(board[0])):
                if cell <= board[x][y]:
                    break
                score += 1
                x, y = x + dx, y + dy
            oob = x not in range(len(board)) or y not in range(len(board[0]))
            score -= oob
            scores.append(score)
            vis.append(oob)
        ans1 += any(vis)
        ans2 = max(ans2, math.prod(scores))
print(ans1)
print(ans2)
