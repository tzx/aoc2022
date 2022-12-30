import re
import z3

lines = [li.strip() for li in open('input.txt')]

p1 = z3.Solver()
p2 = z3.Solver()

monkeys = dict()


def z3var(n):
    if n not in monkeys:
        monkeys[n] = z3.Real(n)
    return monkeys[n]


for li in lines:
    if (m := re.match(r'(\w+): (\w+) ([-+*/]) (\w+)', li)):
        monkey_, dep_a, op, dep_b = m.groups()
        monkey, dep_a, dep_b = z3var(monkey_), z3var(dep_a), z3var(dep_b)
        # Ugliest codemonkey code ever but i don't care
        if monkey_ == 'root':
            p2.add(dep_a == dep_b)
        if op == '*':
            p1.add(monkey == dep_a * dep_b)
            if monkey_ != 'root':
                p2.add(monkey == dep_a * dep_b)
        elif op == '+':
            p1.add(monkey == dep_a + dep_b)
            if monkey_ != 'root':
                p2.add(monkey == dep_a + dep_b)
        elif op == '/':
            p1.add(monkey == dep_a / dep_b)
            if monkey_ != 'root':
                p2.add(monkey == dep_a / dep_b)
        else:
            p1.add(monkey == dep_a - dep_b)
            if monkey_ != 'root':
                p2.add(monkey == dep_a - dep_b)
    else:
        m = re.match(r'(\w+): (\d+)', li)
        assert m
        monkey, num = m.groups()
        p1.add(z3var(monkey) == int(num))
        if monkey != 'humn':
            p2.add(z3var(monkey) == int(num))

print(p1.check())
print(p1.model()[monkeys['root']])

print(p2.check())
print(p2.model()[monkeys['humn']])
