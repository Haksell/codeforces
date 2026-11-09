from collections import Counter

for _ in range(int(input())):
    input()
    s = input()
    cl = Counter()
    cr = Counter(s)
    nl = 0
    res = nr = len(cr)
    for c in s:
        cl[c] += 1
        cr[c] -= 1
        nl = len(cl)
        nr -= cr[c] == 0
        res = max(res, nl + nr)
    print(res)
