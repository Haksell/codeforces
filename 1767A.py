# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive():
    return


def smart(x1, y1, x2, y2, x3, y3):
    xs = {x1, x2, x3}
    ys = {y1, y2, y3}
    return len(set(xs)) == 3 or len(set(ys)) == 3


debug = False
if debug:
    for _ in []:
        args = []
        nn = naive(*args)
        ss = smart(*args)
        if nn != ss:
            print(args, "|", nn, ss)
else:
    for _ in rir():
        read()
        x1, y1 = mir()
        x2, y2 = mir()
        x3, y3 = mir()
        print("YES" if smart(x1, y1, x2, y2, x3, y3) else "NO")

"""
4

4 7
6 8
3 5

4 5
4 7
6 8

5 8
1 8
2 5

3 6
6 6
6 3
"""
