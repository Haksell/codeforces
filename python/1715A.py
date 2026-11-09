for _ in range(int(input())):
    n, m = sorted(map(int, input().split()))
    print(0 if m == 1 else m + n + n - 2)
