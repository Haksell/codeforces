from itertools import count

n = int(input())
t = 0
for i in count(1):
    t += i
    n -= t
    if n < 0:
        print(i - 1)
        break
