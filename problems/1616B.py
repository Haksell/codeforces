# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def double_print(s):
    print(s + s[::-1])


def main():
    for _ in rir():
        n = ir()
        s = input()
        if n == 1 or s[0] == s[1]:
            double_print(s[0])
            continue
        for i in range(n - 1):
            if s[i + 1] > s[i]:
                double_print(s[: i + 1])
                break
        else:
            double_print(s)


if __name__ == "__main__":
    main()
