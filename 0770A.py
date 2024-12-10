# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, k = mir()
    distinct = "".join(chr(97 + i) for i in range(k))
    same = "".join(chr(97 + (i & 1)) for i in range(n - k))
    print(distinct + same)


if __name__ == "__main__":
    main()
