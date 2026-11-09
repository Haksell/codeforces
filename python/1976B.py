def min_last_ops(a, b):
    res = 1 << 30
    for ai, bi in zip(a, b):
        if ai <= last <= bi or ai >= last >= bi:
            return 0
        res = min(res, abs(ai - last), abs(bi - last))
    return res


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    *b, last = list(map(int, input().split()))
    print(sum(abs(ai - bi) for ai, bi in zip(a, b)) + min_last_ops(a, b) + 1)
