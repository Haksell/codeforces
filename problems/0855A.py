# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    cache = set()
    for _ in rir():
        s = input()
        if s in cache:
            print("YES")
        else:
            print("NO")
            cache.add(s)


if __name__ == "__main__":
    main()
