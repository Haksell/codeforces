# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, s):
    groups = [(k, list(v)) for k, v in groupby(s, key=("?".__eq__))]
    if len(groups) == 1:
        return "".join("R" if i & 1 else "B" for i in range(n)) if groups[0][0] else s
    s = list(s)
    si = 0
    for gi, (k, v) in enumerate(groups):
        if not k:
            last = v[-1]
        elif gi == 0:
            ch = s[len(v)]
            for j in range(len(v)):
                ch = "R" if ch == "B" else "B"
                s[len(v) - j - 1] = ch
        else:
            ch = last
            for j in range(len(v)):
                ch = "R" if ch == "B" else "B"
                s[si + j] = ch
        si += len(v)
    return "".join(s)


def main():
    for _ in rir():
        n = ir()
        s = input()
        print(solve(n, s))


if __name__ == "__main__":
    main()
