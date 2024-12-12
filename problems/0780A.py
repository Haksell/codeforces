# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    seen = [False] * (n + 1)
    r = c = 0
    for x in mir():
        if seen[x]:
            c -= 1
        else:
            seen[x] = True
            c += 1
            r = max(r, c)
    print(r)


if __name__ == "__main__":
    main()
