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
        n = ir()
        a = lmir()
        res = [0] * (n + 1)
        dist = 0
        loc = 0
        for i in sorted(range(n), key=a.__getitem__, reverse=True):
            loc = -loc if loc > 0 else -loc + 1
            res[i + 1] = loc
            dist += 2 * a[i] * abs(loc)
        print(dist)
        print(*res)


if __name__ == "__main__":
    main()
