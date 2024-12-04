n = int(input())
a = [2] * (n >> 1)
if n & 1:
    a[-1] = 3
print(len(a))
print(*a)
