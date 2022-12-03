lines = [line.split() for line in open("input.txt")]

res1 = 0
for a, b in lines:
    match a, b:
        case ("A", "X") | ("B", "Y") | ("C", "Z"):
            res1 += 3
        case ("A", "Y") | ("B", "Z") | ("C", "X"):
            res1 += 6
    match b:
        case "X":
            res1 += 1
        case "Y":
            res1 += 2
        case "Z":
            res1 += 3
res2 = 0
for a, b in lines:
    match a, b:
        case ("A", "X") | ("B", "Z") | ("C", "Y"):
            res2 += 3
        case ("A", "Z") | ("B", "Y") | ("C", "X"):
            res2 += 2
        case _:
            res2 += 1
    match b:
        case "Y":
            res2 += 3
        case "Z":
            res2 += 6

print(res1)
print(res2)
