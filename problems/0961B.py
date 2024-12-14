# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, k = mir()
    a = lmir()
    t = lmir()
    s = sum(map(int.__mul__, a, t))
    m = c = sum(a[i] for i in range(k) if not t[i])
    for i in range(k, n):
        if t[i] == 0:
            c += a[i]
        if t[i - k] == 0:
            c -= a[i - k]
        m = max(c, m)
    print(s + m)


if __name__ == "__main__":
    main()
