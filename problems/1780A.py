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
        read()
        a = lmir()
        odds = [i for i, ai in enumerate(a) if ai & 1 == 1]
        evens = [i for i, ai in enumerate(a) if ai & 1 == 0]
        if len(odds) == 0:
            print("NO")
        elif len(odds) >= 3:
            print("YES")
            print(odds[0] + 1, odds[1] + 1, odds[2] + 1)
        elif len(evens) >= 2:
            print("YES")
            print(evens[0] + 1, evens[1] + 1, odds[0] + 1)
        else:
            print("NO")


if __name__ == "__main__":
    main()
