n = int(input())
a = list(map(int, input().split()))
m = -1
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        m = max(m, a[i:j].count(0) - a[i:j].count(1))
print(m + a.count(1))
