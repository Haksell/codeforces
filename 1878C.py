for _ in range(int(input())):
    n, k, x = map(int, input().split())
    mini = k * (k + 1) >> 1
    maxi = ((n - k + 1) + n) * k >> 1
    print("YES" if mini <= x <= maxi else "NO")
