lines = [li.strip() for li in open('input.txt')]

mtch = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

values = []
for li in lines:
    res = 0
    for i, ch in enumerate(reversed(li)):
        res += (5 ** i) * mtch[ch]
    values.append(res)
nu = sum(values)

res = ''
while nu != 0:
    nu, b = divmod(nu + 2, 5)
    res += '=-012'[b]

print(sum(values))
print(res[::-1])
