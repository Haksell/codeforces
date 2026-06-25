# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _, m, r = mir()
    s = min(mir())
    b = max(mir())
    if s >= b:
        print(r)
    else:
        q, m = divmod(r, s)
        print(q * b + m)


if __name__ == "__main__":
    main()
