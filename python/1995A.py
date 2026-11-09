def solve(n, k):
    if k == 0:
        return 0
    if k <= n:
        return 1
    k -= n
    res = 1
    for i in range(n - 1, 0, -1):
        if k <= i:
            return res + 1
        if k <= 2 * i:
            return res + 2
        k -= 2 * i
        res += 2


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))
