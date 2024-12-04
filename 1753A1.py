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
        if n % 2 == 1:
            print(-1)
            continue
        res = []
        for i in range(0, n, 2):
            if a[i] == a[i + 1]:
                res.append((i + 1, i + 2))
            else:
                res.append((i + 1, i + 1))
                res.append((i + 2, i + 2))
        print(len(res))
        for l, r in res:
            print(l, r)


if __name__ == "__main__":
    main()
