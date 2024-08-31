import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mir()
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
    weights = input()

    root = weights[0]
    leaves = [w for i, w in enumerate(weights) if i != 0 and len(tree[i]) == 1]
    waiting = sum(
        w == "?" for i, w in enumerate(weights) if i != 0 and len(tree[i]) != 1
    )
    # print("w", waiting)
    qs = leaves.count("?")
    zs = leaves.count("0")
    os = leaves.count("1")
    if root == "?":
        if qs == 0:
            print(max(zs, os))
        elif os == zs:
            if waiting & 1 == 0:
                if qs & 1 == 0:
                    print(os + qs // 2)
                else:
                    print(os + qs // 2)
            else:
                if qs & 1 == 0:
                    print(os + qs // 2)
                else:
                    print(os + qs // 2 + 1)
        else:
            print(max(os, zs) + qs // 2)
    else:
        diff = zs if root == "1" else os
        print(diff + (qs + 1) // 2)

""" 011101110
9
2
1 2
00
2
1 2
01
2
1 2
0?
2
1 2
10
2
1 2
11
2
1 2
1?
2
1 2
?0
2
1 2
?1
2
1 2
??
"""

""" 211121111
9
3
1 2
1 3
?00
3
1 2
1 3
?01
3
1 2
1 3
?0?
3
1 2
1 3
?10
3
1 2
1 3
?11
3
1 2
1 3
?1?
3
1 2
1 3
??0
3
1 2
1 3
??1
3
1 2
1 3
???
"""

""" 110110111
9
3
1 2
2 3
?00
3
1 2
2 3
?01
3
1 2
2 3
?0?
3
1 2
2 3
?10
3
1 2
2 3
?11
3
1 2
2 3
?1?
3
1 2
2 3
??0
3
1 2
2 3
??1
3
1 2
2 3
???
"""
