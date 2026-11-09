for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(2 * (n - max(a)) - k + 1)
