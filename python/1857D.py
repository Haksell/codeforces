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
        a = lmir()
        b = lmir()
        m = max(map(int.__sub__, a, b))
        res = [i + 1 for i in range(n) if a[i] - b[i] == m]
        print(len(res))
        print(*res)


if __name__ == "__main__":
    main()
