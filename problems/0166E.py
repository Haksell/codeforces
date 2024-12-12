# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 1_000_000_007


def matmul(a1, b1, c1, d1, a2, b2, c2, d2):
    return (
        (a1 * a2 + b1 * c2) % MOD,
        (a1 * b2 + b1 * d2) % MOD,
        (c1 * a2 + d1 * c2) % MOD,
        (c1 * b2 + d1 * d2) % MOD,
    )


def matpow(ma, mb, mc, md, n):
    ra, rb, rc, rd = 1, 0, 0, 1
    while n:
        if n & 1:
            ra, rb, rc, rd = matmul(ra, rb, rc, rd, ma, mb, mc, md)
        ma, mb, mc, md = matmul(ma, mb, mc, md, ma, mb, mc, md)
        n >>= 1
    return ra, rb, rc, rd


def main():
    print(matpow(0, 1, 3, 2, ir())[0])


if __name__ == "__main__":
    main()
