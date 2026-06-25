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
        n, d, h = mir()
        prev = -h
        r = d * h * h * n
        for y in mir():
            if y - prev < h:
                rem_h = h - y + prev
                rem_w = d * rem_h
                r -= rem_h * rem_w
            prev = y
        print(r / 2 / h)


if __name__ == "__main__":
    main()
