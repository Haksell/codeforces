# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    x = lmir()
    cnt = [0] * (2 * n + 1)
    for xi in x:
        cnt[xi] += 1
    r = 0 if k & 1 else cnt[k >> 1] >> 1
    for i in range((k + 1) >> 1):
        j = k - i
        r += min(cnt[i], cnt[j])
    print(r)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
