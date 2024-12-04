n, m = map(int, input().split())
l = sorted(map(int, input().split()))
print(min(l[i + n - 1] - l[i] for i in range(m - n + 1)))