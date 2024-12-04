from itertools import groupby
from sys import stdin

stdin.readline()
print(sum(1 for _ in groupby(stdin.read().split())))