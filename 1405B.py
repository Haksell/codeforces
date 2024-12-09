# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    stock = 0
    for ai in a:
        if ai < 0:
            diff = min(stock, -ai)
            ai += diff
            stock -= diff
            ans -= ai
        else:
            stock += ai
    print(ans)
