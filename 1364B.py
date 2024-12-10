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
        res = a[:2]
        increasing = res[1] > res[0]
        for i in range(2, n):
            if increasing == (a[i] > a[i - 1]):
                res[-1] = a[i]
            else:
                res.append(a[i])
                increasing = not increasing
        print(len(res))
        print(*res)


if __name__ == "__main__":
    main()
