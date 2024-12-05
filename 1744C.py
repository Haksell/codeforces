# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, c = input().split()
    n = int(n)
    s = input()
    if c == "g":
        print(0)
    else:
        nxt = [-1] * n
        gi = -1
        while True:
            prev = gi
            gi = s.find("g", gi + 1)
            if gi == -1:
                for i in range(prev + 1, n):
                    nxt[i] = nxt[0]
                break
            for i in range(prev + 1, gi + 1):
                nxt[i] = gi
        print(max((nxt[i] - i) % n for i, si in enumerate(s) if si == c))
