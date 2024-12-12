# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, x = mir()
        a = lmir()
        res = 0
        cur = 0
        for ai in sorted(a, reverse=True):
            if ai * (cur + 1) >= x:
                res += 1
                cur = 0
            else:
                cur += 1
        print(res)


if __name__ == "__main__":
    main()
