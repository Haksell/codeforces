# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    a = lmir()
    left = [0] * n
    right = [0] * n
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            left[i] = left[i - 1] + 1
        if a[~i] >= a[~(i - 1)]:
            right[~i] = right[~(i - 1)] + 1
    print(max(map(int.__add__, left, right)) + 1)


if __name__ == "__main__":
    main()
