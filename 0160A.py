n = int(input())
a = sorted(map(int, input().split()))
s = sum(a)
n = 0
i = 0
while n + n <= s:
    n += a.pop()
    i += 1
print(i)
