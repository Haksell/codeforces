# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def is_diverse(s):
    n = len(s)
    return len(set(s)) == n and ord(max(s)) - ord(min(s)) == n - 1


def main():
    for _ in rir():
        s = input()
        print("YES" if is_diverse(s) else "NO")


if __name__ == "__main__":
    main()
