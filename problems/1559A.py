# ruff: noqa: E731, E741
from functools import reduce
from operator import and_

for _ in range(int(input())):
    input()
    print(reduce(and_, map(int, input().split())))
