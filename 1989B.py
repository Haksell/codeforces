# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(a, b):
    bi = 0
    for ai in a:
        if ai == b[bi]:
            bi += 1
            if bi == len(b):
                break
    return bi


def main():
    for _ in rir():
        a = input()
        b = input()
        print(
            len(a)
            + len(b)
            - max(
                (f(a, b[i:]) for i in range(len(b))),
                default=0,
            )
        )


if __name__ == "__main__":
    main()
