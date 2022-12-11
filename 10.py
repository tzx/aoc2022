lines = [li.strip() for li in open("input.txt")]

stack = []
reg = 1
for li in lines:
    match li.split():
        case "addx", val:
            stack.extend([reg, reg])
            reg += int(val)
        case ["noop"]:
            stack.append(reg)
        case _:
            assert False
print(sum(cycle * stack[cycle - 1] for cycle in [20, 60, 100, 140, 180, 220]))

for i, val in enumerate(stack):
    print("#" if i % 40 in range(val - 1, val + 2) else " ",
          end="\n" if i % 40 == 39 else "")
