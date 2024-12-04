n, length = map(int, input().split())
a = sorted(map(int, input().split()))
print(max(a[0], *((b - a) / 2 for a, b in zip(a, a[1:])), length - a[-1]))
