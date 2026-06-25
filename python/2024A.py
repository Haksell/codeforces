# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def clamp(x, mini, maxi):
    return mini if x < mini else maxi if x > maxi else x


def main():
    for _ in rir():
        a, b = mir()
        print(clamp(2 * a - b, 0, a))


if __name__ == "__main__":
    main()
