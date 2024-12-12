# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    s = input()
    t = input()
    last = {c: i for i, c in enumerate(t[:-1])}
    best = -(1 << 30)
    si = ti = 0
    for i, c in enumerate(s[1:], 1):
        if c in last:
            j = last[c]
            if j - i > best:
                best = j - i
                si = i
                ti = j
    print(-1 if best == -(1 << 30) else s[:si] + t[ti:])


if __name__ == "__main__":
    main()
