# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _, k = mir()
    a = input().split()
    print(sum(ai.count("4") + ai.count("7") <= k for ai in a))


if __name__ == "__main__":
    main()
