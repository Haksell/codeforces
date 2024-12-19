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
        n = ir()
        s = input()
        i = s.find("8")
        print("YES" if i >= 0 and i + 10 < n else "NO")


if __name__ == "__main__":
    main()
