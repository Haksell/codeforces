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
        mn = min(a)
        print("YES" if a.count(mn) == 1 or any(ai % mn for ai in a) else "NO")


if __name__ == "__main__":
    main()
