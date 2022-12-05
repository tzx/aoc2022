import re
lines = [li.strip() for li in open("input.txt")]

ans = 0
ans2 = 0
res = []

for li in lines:
    s1, e1, s2, e2 = map(int, re.findall(r'\d+', li))
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        ans += 1
    if s2 <= e1 and e2 >= s1:
        ans2 += 1

print(ans)
print(ans2)
