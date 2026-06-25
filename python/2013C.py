# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def q(s):
    print("?", s)
    sys.stdout.flush()
    res = input() == "1"
    sys.stdout.flush()
    return res


def solve(n):
    if not q("0"):
        return "1" * n
    res = "0"
    while len(res) < n - 1:
        if q(res + "0"):
            res = res + "0"
            continue
        if "0" + res != res + "0" and q("0" + res):
            res = "0" + res
            continue
        if q("1" + res + "1"):
            res = "1" + res + "1"
            continue
        if q(res + "1"):
            res = res + "1"
            while len(res) < n:
                res += "0" if q(res + "0") else "1"
            return res
        else:
            res = "1" + res
            while len(res) < n:
                res = ("0" if q("0" + res) else "1") + res
            return res
    if len(res) == n:
        return res
    for s in (res + "0", res + "1", "0" + res):
        if q(s):
            return s
    return "1" + res


for _ in rir():
    print("!", solve(ir()))
    sys.stdout.flush()
