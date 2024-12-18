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
        x = input()
        y = input()
        for i, (cx, cy) in enumerate(zip(x, y)):
            if cx != cy:
                print(x[:i] + max(cx, cy) + "".join(map(min, x[i + 1 :], y[i + 1 :])))
                print(y[:i] + min(cx, cy) + "".join(map(max, x[i + 1 :], y[i + 1 :])))
                break
        else:
            print(x)
            print(y)


if __name__ == "__main__":
    main()
