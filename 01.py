li = [l.strip() for l in open("input.txt").read().split('\n\n')]
res = []
for l in li:
    r = sum([int(a) for a in l.split('\n')])
    res.append(r)

res = sorted(res)
print(sum(res[-3:]))
