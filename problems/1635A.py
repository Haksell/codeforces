# ruff: noqa: E731, E741
from functools import reduce
from operator import or_

for _ in range(int(input())):
    input()
    print(reduce(or_, map(int, input().split())))
