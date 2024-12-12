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
        if n == 1:
            print(1)
            continue
        if n <= 4:
            print(2)
            continue
        res = 2
        i = 1
        while i < n:
            i = 2 * i + 2
            res += 1
        print(res - 1)


if __name__ == "__main__":
    main()
