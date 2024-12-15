# ruff: noqa: E731, E741
import re
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def ev(e):
    res = 0
    plus = True
    prev_is_op = True
    for x in re.findall(r"[-+]|\d+", e):
        if x != "0" and x[0] == "0":
            return
        if len(x) > 10:
            return
        if x == "+":
            if prev_is_op:
                return
            plus = True
            prev_is_op = True
        elif x == "-":
            if prev_is_op:
                return
            plus = False
            prev_is_op = True
        elif plus:
            res += int(x)
            prev_is_op = False
        else:
            res -= int(x)
            prev_is_op = False
    if prev_is_op:
        return
    return res


def check(s):
    a, b = s.split("=")
    if not a or not b:
        return False
    eva = ev(a)
    evb = ev(b)
    return eva is not None and evb is not None and eva == evb


def main():
    s = input()
    if check(s):
        print("Correct")
        return
    for i, c in enumerate(s):
        if not c.isdigit():
            continue
        si = s[:i] + s[i + 1 :]
        for j in range(len(s)):
            sj = si[:j] + c + si[j:]
            if check(sj):
                print(sj)
                return
    print("Impossible")


if __name__ == "__main__":
    main()
