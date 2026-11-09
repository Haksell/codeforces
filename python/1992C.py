for _ in range(int(input())):
    n, m, k = map(int, input().split())
    res = list(range(n, m, -1)) + list(range(1, m + 1))
    print(*res)
