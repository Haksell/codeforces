# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(s):
    s = list(map(int, s))
    c2 = s.count(2)
    c3 = s.count(3)
    s = sum(s)
    for i2 in range(min(c2 + 1, 9)):
        for i3 in range(min(c3 + 1, 3)):
            if (s + i2 * 2 + i3 * 6) % 9 == 0:
                return True
    return False


def main():
    for _ in rir():
        s = input()
        print("YES" if solve(s) else "NO")


if __name__ == "__main__":
    main()
