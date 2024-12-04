for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m * min(n - 1, 2))
