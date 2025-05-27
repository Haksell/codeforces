# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m, _ = mir()
    a = lmir()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mir()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    even = [None] * n
    odd = [None] * n
    d = 0
    q = [0]
    while q:
        cur = odd if d & 1 else even
        nq = []
        for u in q:
            if cur[u] is None:
                cur[u] = d
                for v in g[u]:
                    nq.append(v)
        q = nq
        d += 1

    s = sum(a)
    if all(x & 1 == 0 for x in a):
        print(
            "".join(
                "1" if even[i] is not None and even[i] <= s else "0" for i in range(n)
            )
        )
    else:
        cur = odd if s & 1 else even
        opp = even if s & 1 else odd
        se = sum(a) - min(x for x in a if x & 1)
        print(
            "".join(
                "1"
                if (cur[i] is not None and cur[i] <= s)
                or (opp[i] is not None and opp[i] <= se)
                else "0"
                for i in range(n)
            )
        )


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
