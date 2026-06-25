# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, read().split()))
    print(max(sum(1 for _ in v) for _, v in groupby(a)))
