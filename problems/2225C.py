# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    s = input()
    t = input()

    res = 0

    i = 0
    while i < n - 1:
        if s[i] == t[i]:
            i += 1
            continue
        if s[i] == s[i + 1]:
            res += t[i] != t[i + 1]
            i += 2
        elif t[i] == t[i + 1]:
            res += 1
            i += 2
        else:
            res += 1
            i += 1

    if i == n - 1:
        res += s[-1] != t[-1]

    print(res)


def main():
    for _ in rir():
        solve()


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()