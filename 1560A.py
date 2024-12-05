# ruff: noqa: E731, E741
from itertools import count

valid = []
for i in count(1):
    if i % 3 != 0 and i % 10 != 3:
        valid.append(i)
        if len(valid) == 1000:
            break

for _ in range(int(input())):
    print(valid[int(input()) - 1])
