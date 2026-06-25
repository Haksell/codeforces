# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 1_000_000_007


def depth(tree, node, parent):
    x = 1
    while len(tree[node]) == 2:
        parent, node = node, next(c for c in tree[node] if c != parent)
        x += 1
    return x


def solve():
    n = ir()
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mir()
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
    leaves = [i for i in range(1, n) if len(tree[i]) == 1]
    if len(leaves) >= 3:
        return 0
    if len(leaves) == 1:
        return pow(2, n, MOD)
    branch = next((i for i in range(n) if len(tree[i]) == 3), 0)
    parent = None
    node = 0
    stig = 0
    while node != branch:
        parent, node = node, next(c for c in tree[node] if c != parent)
        stig += 1
    c1, c2 = [c for c in tree[branch] if c != parent]
    l1, l2 = depth(tree, c1, branch), depth(tree, c2, branch)
    return (4 if l1 == l2 else 3) * pow(2, abs(l1 - l2) + stig, MOD) % MOD


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
