# ruff: noqa: E731, E741
from itertools import count
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    s = list(map(int, input()))
    zeros = len(s) - sum(s)
    res = 0
    for i in count(1):
        if zeros == 0:
            print(res)
            return
        for j in range(i - 1, n, i):
            if s[j] == 1:
                break
            if s[j] == 0:
                zeros -= 1
                res += i
                s[j] = 2


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
