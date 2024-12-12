# ruff: noqa: E731, E741
from functools import cache
from itertools import product
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def bruteforce(s):
    @cache
    def helper(s, alice, can_wait):
        if all(c == "1" for c in s):
            return 0
        elif alice:
            res = (
                max(
                    helper(s[:i] + "1" + s[i + 1 :], not alice, True)
                    for i, c in enumerate(s)
                    if c == "0"
                )
                - 1
            )
            if can_wait and s != s[::-1]:
                res = max(res, helper(s, not alice, False))
            return res
        else:
            res = (
                min(
                    helper(s[:i] + "1" + s[i + 1 :], not alice, True)
                    for i, c in enumerate(s)
                    if c == "0"
                )
                + 1
            )
            if can_wait and s != s[::-1]:
                res = min(res, helper(s, not alice, False))
            return res

    score = helper(s, True, True)
    return "ALICE" if score > 0 else "BOB" if score < 0 else "DRAW"


def solve(s):
    n = len(s)
    d = sum(s[i] != s[~i] for i in range(n >> 1))
    z = s.count("0")
    if z == 0 or (z == 2 and d == 1):
        return "DRAW"
    elif d == 0 and (n & 1 == 0 or s[n >> 1] != "0" or z == 1):
        return "BOB"
    else:
        return "ALICE"


def main():
    if sys.stdin.isatty():
        for i in range(1, 11):
            for s in product("01", repeat=i):
                s = "".join(s)
                b = bruteforce(s)
                r = solve(s)
                assert b == r, (s, b, r)
                print(s, b)
    else:
        for _ in rir():
            read()
            print(solve(input()))


if __name__ == "__main__":
    main()
