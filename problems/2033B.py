# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = [lmir() for _ in range(n)]
        res = max(0, -min(a[i][i] for i in range(n)))
        for k in range(1, n):
            res += max(0, -min(a[i + k][i] for i in range(n - k)))
            res += max(0, -min(a[i][i + k] for i in range(n - k)))
        print(res)


if __name__ == "__main__":
    main()
