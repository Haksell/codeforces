# ruff: noqa: E731, E741
import sys

for _ in range(int(sys.stdin.readline())):
    h = int(sys.stdin.readline()) >> 1
    a = list(map(int, sys.stdin.readline().split()))
    mini = min(a)
    for x in a:
        if x == mini:
            continue
        print(x, mini)
        h -= 1
        if h == 0:
            break
