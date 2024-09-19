# ruff: noqa: E731, E741

import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(tree, weights):
    root = weights[0]
    leaves = [w for i, w in enumerate(weights) if i != 0 and len(tree[i]) == 1]
    waiting = sum(
        w == "?" for i, w in enumerate(weights) if i != 0 and len(tree[i]) != 1
    )
    qs = leaves.count("?")
    zs = leaves.count("0")
    os = leaves.count("1")
    if root != "?":
        diff = zs if root == "1" else os
        return diff + (qs + 1) // 2
    elif qs == 0:
        return max(zs, os)
    elif os == zs:
        return os + qs // 2 + (waiting & qs & 1)
    else:
        return max(os, zs) + qs // 2


def main():
    for _ in rir():
        n = ir()
        tree = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = mir()
            tree[u - 1].append(v - 1)
            tree[v - 1].append(u - 1)
        weights = input()
        print(solve(tree, weights))


if __name__ == "__main__":
    main()
