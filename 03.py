import string

lines = [l.strip() for l in open('input.txt')]
sc = lambda x: ord(x) - ord('a') + 1 if x in string.ascii_lowercase else ord(
    x) - ord('A') + 27
ans = 0

for l in lines:
    a, b = l[:len(l) // 2], l[len(l) // 2:]
    cmn = set(a) & set(b)
    ans += sc(cmn.pop())
print(ans)

ans2 = 0
for i in range(0, len(lines), 3):
    l1, l2, l3 = lines[i], lines[i + 1], lines[i + 2]
    cmn = set(l1) & set(l2) & set(l3)
    ans2 += sc(cmn.pop())
print(ans2)
