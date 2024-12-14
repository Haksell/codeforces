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
        n, k, x = mir()
        a = sorted(mir())
        res = cur = sum(a[:-x]) - sum(a[-x:])
        for i in range(k):
            cur += a[~i]
            if i + x < n:
                cur -= 2 * a[~(i + x)]
            res = max(res, cur)
        print(res)


if __name__ == "__main__":
    main()
