# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

VOWELS = "aeiou"


def main():
    for _ in rir():
        n = ir()
        print("".join((n + i) // 5 * c for i, c in enumerate(VOWELS)))


if __name__ == "__main__":
    main()
