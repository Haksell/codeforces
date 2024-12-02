# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    v, e = mir()
    g = [[] for _ in range(v)]
    for _ in range(e):
        i, j = mir()
        g[i - 1].append(j - 1)
        g[j - 1].append(i - 1)
    res = 0
    seen = [False] * v
    for i in range(v):
        if seen[i]:
            continue
        st = [i]
        is_cycle = True
        while st:
            node = st.pop()
            if len(g[node]) != 2:
                is_cycle = False
            for nb in g[node]:
                if seen[nb]:
                    continue
                seen[nb] = True
                st.append(nb)
        res += is_cycle
    print(res)


if __name__ == "__main__":
    main()
