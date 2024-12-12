# ruff: noqa: E731, E741
from itertools import count

for _ in range(int(input())):
    _, x = map(int, input().split())
    a = set(map(int, input().split()))
    for i in count(1):
        if i not in a:
            x -= 1
            if x == 0:
                while i + 1 in a:
                    i += 1
                print(i)
                break
