# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b, s = mir()
    print("Yes" if abs(a) + abs(b) <= s and (a ^ b ^ s) & 1 == 0 else "No")


if __name__ == "__main__":
    main()
