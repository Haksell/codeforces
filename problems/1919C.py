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
        if n <= 2:
            print(0)
            continue
        s = t = 1 << 20
        p = 0
        for ai in a:
            if s == ai or t == ai:
                continue
            if ai > s >= t:
                t = ai
                p += 1
            elif ai > t >= s:
                s = ai
                p += 1
            elif s > ai > t:
                s = ai
            elif t > ai > s:
                t = ai
            elif s >= t > ai:
                t = ai
            elif t >= s > ai:
                s = ai
        print(p)


if __name__ == "__main__":
    main()
