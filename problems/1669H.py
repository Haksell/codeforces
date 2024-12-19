# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

BITS = 31


def main():
    for _ in rir():
        n, k = mir()
        a = lmir()
        cnt = [0] * BITS
        for ai in a:
            for i in range(BITS):
                cnt[i] += ai & 1
                ai >>= 1
        r = 0
        for i in reversed(range(BITS)):
            if cnt[i] + k >= n:
                r |= 1 << i
                k -= n - cnt[i]
        print(r)


if __name__ == "__main__":
    main()
