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
        n, r, b = mir()
        s = ["R"] * n
        short, longs = divmod(r, b + 1)
        i = -1
        for j in range(b):
            i += short + (j < longs) + 1
            s[i] = "B"
        print("".join(s))


if __name__ == "__main__":
    main()
