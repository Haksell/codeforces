# ruff: noqa: E731, E741
from collections import deque
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, k):
    if n <= 50 and k >= 2 ** (n - 1):
        return None
    lo = 0
    hi = n - 1
    r = [-1] * n
    bits = deque()
    while k:
        bits.append(k & 1)
        k >>= 1
    bits.reverse()
    while len(bits) < n - 1:
        bits.appendleft(0)
    for i in range(1, n):
        if bits[i - 1]:
            r[hi] = i
            hi -= 1
        else:
            r[lo] = i
            lo += 1
    r[lo] = n
    return r


def main():
    for _ in rir():
        n, k = mir()
        k -= 1
        if r := solve(n, k):
            print(*r)
        else:
            print(-1)


if __name__ == "__main__":
    main()
