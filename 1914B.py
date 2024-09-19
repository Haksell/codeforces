for _ in range(int(input())):
    n, k = map(int, input().split())
    res = list(range(1, k + 1)) + list(range(n, k, -1))
    print(*res)
