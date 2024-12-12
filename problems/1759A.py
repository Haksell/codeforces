# ruff: noqa: E731, E741
from itertools import cycle
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: list(map(int, read().split()))
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    s = input()
    if not set(s) <= set("Yes"):
        print("NO")
    else:
        c = (
            cycle("Yes")
            if s[0] == "Y"
            else cycle("esY")
            if s[0] == "e"
            else cycle("sYe")
        )
        print("YES" if all(a == b for a, b in zip(s, c)) else "NO")
