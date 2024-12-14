# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b = mir()
    r = m = 0
    while a:
        r += a
        m += a
        a, m = divmod(m, b)
    print(r)


if __name__ == "__main__":
    main()
