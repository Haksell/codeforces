# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, s):
    pi = s.find("p")
    si = s.rfind("s")
    if pi == -1 or si == -1:
        return True
    if pi < si:
        return False
    return si == 0 or pi == n - 1


def main():
    for _ in rir():
        n = ir()
        s = input()
        print("YES" if solve(n, s) else "NO")


if __name__ == "__main__":
    main()
