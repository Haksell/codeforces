# ruff: noqa: E731, E741
from collections import deque

for _ in range(int(input())):
    input()
    d = deque(map(int, input().split()))
    a = b = last = cur = m = 0
    left = True
    while d:
        if left:
            while d and cur <= last:
                cur += d.popleft()
            a += cur
        else:
            while d and cur <= last:
                cur += d.pop()
            b += cur
        left = not left
        last = cur
        cur = 0
        m += 1
    print(m, a, b)
