# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    _, k, l = mir()
    a = lmir()
    t = a[0]
    c = k
    for s in a[1:]:
        if c >= l:
            return round(2 * t)
        if s - c >= t:
            nt = min((s - c - t) / 2, l - c)
            t += nt
            c += nt + k
        elif s + t <= c:
            c = s + t + k
        else:
            c += k
    t += max(0, l - c)
    return round(2 * t)


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
