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
        a = 0
        b = 0
        a_big = False
        for d in map(int, input()):
            h = d >> 1
            a *= 10
            b *= 10
            a += h
            b += h
            if d & 1:
                if a_big:
                    b += 1
                    a_big = False
                else:
                    a += 1
                    a_big = True
        print(a, b)


if __name__ == "__main__":
    main()
