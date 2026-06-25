# ruff: noqa: E731, E741
for _ in range(int(input())):
    b = True
    lp = lc = 0
    for _ in range(int(input())):
        p, c = map(int, input().split())
        dp, dc = p - lp, c - lc
        if dp < 0 or dc < 0 or dc > dp:
            b = False
        lp, lc = p, c
    print("YES" if b else "NO")
