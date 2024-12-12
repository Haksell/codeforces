# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(a, b, c):
    r = range(len(a))
    ma = max(r, key=lambda i: a[i])
    mb = max(r, key=lambda i: i != ma and b[i])
    mc = max(r, key=lambda i: i != ma and i != mb and c[i])
    return a[ma] + b[mb] + c[mc]


def main():
    for _ in rir():
        _ = ir()
        a = lmir()
        b = lmir()
        c = lmir()
        print(
            max(f(a, b, c), f(a, c, b), f(b, a, c), f(b, c, a), f(c, a, b), f(c, b, a))
        )


if __name__ == "__main__":
    main()
