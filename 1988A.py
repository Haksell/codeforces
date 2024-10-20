for _ in range(int(input())):
    n, k = map(int, input().split())
    print((n + k - 3) // (k - 1))
