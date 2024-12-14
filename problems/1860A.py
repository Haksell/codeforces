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
        s = input()
        x1 = "()" * len(s)
        x2 = "(" * len(s) + ")" * len(s)
        print(f"YES\n{x1}" if s not in x1 else f"YES\n{x2}" if s not in x2 else "NO")


if __name__ == "__main__":
    main()
