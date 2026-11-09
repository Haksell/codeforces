for _ in range(int(input())):
    res = 4
    prev = 1
    for c in map(int, input()):
        if c == 0:
            c = 10
        res += abs(c - prev)
        prev = c
    print(res)
