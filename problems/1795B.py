# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, k = mir()
        start = end = False
        for _ in range(n):
            l, r = mir()
            start = start or l == k
            end = end or r == k
        print("YES" if start and end else "NO")


if __name__ == "__main__":
    main()
