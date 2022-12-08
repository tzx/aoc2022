from collections import defaultdict
lines = [li.strip() for li in open("input.txt")]

dir_stack = []
sizes = defaultdict(int)
for li in lines:
    match li.split():
        case "$", "cd", "/":
            dir_stack = []
        case "$", "cd", "..":
            dir_stack.pop()
        case "$", "cd", ddd:
            dir_stack.append(ddd)
        case ("dir", _) | ("$", "ls"):
            pass
        case size, filename:
            for i in range(len(dir_stack)):
                sizes['/'.join(dir_stack[:i+1])] += int(size)
            sizes['/'] += int(size)
ans1 = sum(size for dirr, size in sizes.items() if size <= 100000)
print(ans1)
total_used = sizes['/']
needed = 70000000 - 30000000
ans2 = min(size for dirr, size in sizes.items() if size >= total_used - needed)
print(ans2)
