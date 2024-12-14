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
        if k == 1:
            print(n)
            continue
        res = 0
        while n:
            n, d = divmod(n, k)
            res += d
        print(res)


if __name__ == "__main__":
    main()
