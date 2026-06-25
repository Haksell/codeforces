# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def possible(a, b, k, cookies):
    for ai, bi in zip(a, b):
        k -= max(0, ai * cookies - bi)
        if k < 0:
            return False
    return True


def main():
    _, k = mir()
    a = lmir()
    b = lmir()
    lo = 0
    hi = 1 << 32
    while lo + 1 < hi:
        mi = lo + hi >> 1
        if possible(a, b, k, mi):
            lo = mi
        else:
            hi = mi
    print(lo)


if __name__ == "__main__":
    main()
