# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def is_balanced(s):
    n = 0
    for c in s:
        if c == "(":
            n += 1
        else:
            n -= 1
            if n < 0:
                return False
    return n == 0


def solve():
    s = input()
    i = next(i for i in range(len(s)) if s[i] == "(")
    j = next(i for i in reversed(range(len(s))) if s[i] == ")")
    t = [c for k, c in enumerate(s) if k != i and k != j]
    print("NO" if is_balanced(t) else "YES")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
