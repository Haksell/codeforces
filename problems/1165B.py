# ruff: noqa: E731, E741
from itertools import count

n = int(input())
a = sorted(map(int, input().split()), reverse=True)
for i in count(1):
    while a and a[-1] < i:
        a.pop()
    if not a:
        print(i - 1)
        break
    a.pop()
else:
    print(n)
