import re
import operator
import math
from collections import deque
from copy import deepcopy

blocks = open("input.txt").read().split("\n\n")

monkeys_ = []
get_numbers = lambda x: list(map(int, re.findall(r"\d+", x)))
for block in blocks:
    _, st, op_, div_test, true_throw, false_throw = block.strip().split('\n')
    st = deque(get_numbers(st))
    op = operator.add if "+" in op_ else operator.mul
    op_right, = get_numbers(op_) if get_numbers(op_) else (None, )
    div_test, = get_numbers(div_test)
    true_throw, = get_numbers(true_throw)
    false_throw, = get_numbers(false_throw)
    monkeys_.append({
        "st": st,
        "op": op,
        "op_right": op_right,
        "div_test": div_test,
        "true_throw": true_throw,
        "false_throw": false_throw
    })

lcm = math.lcm(*[monkey["div_test"] for monkey in monkeys_])

for run in [20, 10000]:
    monkeys = deepcopy(monkeys_)
    inspected = [0 for _ in monkeys]
    for _ in range(run):
        for i, monkey in enumerate(monkeys):
            while monkey["st"]:
                num = monkey["st"].popleft()
                op_right = monkey["op_right"] if monkey["op_right"] else num
                new = monkey["op"](num, op_right)
                new = new // 3 if run == 20 else new % lcm
                to_throw = monkey["true_throw"] if new % monkey[
                    "div_test"] == 0 else monkey["false_throw"]
                monkeys[to_throw]["st"].append(new)
                inspected[i] += 1
    sorted_ = sorted(inspected)
    print(sorted_[-1] * sorted_[-2])
