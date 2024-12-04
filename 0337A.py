n, m = map(int, input().split())
a = sorted(map(int, input().split()))
print(min(a[i + n - 1] - a[i] for i in range(m - n + 1)))
