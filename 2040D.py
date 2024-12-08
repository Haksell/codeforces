# ruff: noqa: E731, E741
from math import isqrt
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    N = 400_001
    sieve = [True] * N
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(N) + 1):
        if sieve[i]:
            for j in range(i * i, N, i):
                sieve[j] = False
    for _ in rir():
        n = ir()
        t = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = mir()
            t[u - 1].append(v - 1)
            t[v - 1].append(u - 1)
        available = [True] * (2 * n + 1)
        available[0] = available[1] = False
        st = [0]
        r = [-1] * n
        r[0] = 1
        while st:
            i = st.pop()
            for j in t[i]:
                if r[j] != -1:
                    continue
                while True:
                    x = randint(1, 2 * n)
                    if available[x] and not sieve[abs(x - r[i])]:
                        break
                available[x] = False
                r[j] = x
                st.append(j)
        print(*r)


if __name__ == "__main__":
    main()
