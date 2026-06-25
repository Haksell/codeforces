# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    f = randint(1, 1 << 30)

    n = ir()
    a = lmir()
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mir()
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    res = [0] * n
    stack = [(0, None, None)]
    while stack:
        node, parent, gp = stack.pop()

        for old in (parent, gp):
            if old is not None and a[node] == a[old]:
                res[a[node] - 1] = 1

        seen = set()
        for child in tree[node]:
            if child != parent:
                if a[child] + f in seen:
                    res[a[child] - 1] = 1
                seen.add(a[child] + f)
                stack.append((child, node, parent))

    print("".join(map(str, res)))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
