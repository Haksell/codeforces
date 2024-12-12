# ruff: noqa: E731, E741
from itertools import count

n = int(input())
for i in count(19, 9):
    if sum(map(int, str(i))) == 10:
        n -= 1
        if n == 0:
            print(i)
            break
