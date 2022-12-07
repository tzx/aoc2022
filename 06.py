inn = open("input.txt").read().strip()
AMTS = [4, 14]
for AMT in AMTS:
    for i in range(len(inn)):
        if len(set(inn[i: i + AMT])) == AMT:
            print(i + AMT)
            break
