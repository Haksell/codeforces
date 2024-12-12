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
        a = list(map(int, input()))
        b = list(map(int, input()))
        res = []
        for i in range(n - 1):
            if a[i] != a[i + 1]:
                res.append(i + 1)
        cur = a[-1]
        for i in reversed(range(n)):
            if b[i] != cur:
                res.append(i + 1)
                cur = 1 - cur
        print(len(res), *res)


if __name__ == "__main__":
    main()
