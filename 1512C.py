# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a, b, s):
    s = list(s)
    n = a + b
    h = n >> 1
    qs = []
    for i in range(h):
        if s[i] == s[~i] == "?":
            qs.append(i)
            continue
        if s[i] == "?":
            s[i] = s[~i]
        elif s[~i] == "?":
            s[~i] = s[i]
        if s[i] == s[~i] == "0":
            a -= 2
        elif s[i] == s[~i] == "1":
            b -= 2
        else:
            return None
    if n & 1:
        if s[h] == "0":
            a -= 1
        elif s[h] == "1":
            b -= 1
        elif a & 1:
            a -= 1
            s[h] = "0"
        else:
            b -= 1
            s[h] = "1"
    if a < 0 or b < 0 or a & 1 or b & 1:
        return None
    for i in qs:
        if a:
            s[i] = s[~i] = "0"
            a -= 2
        else:
            s[i] = s[~i] = "1"
    return "".join(s)


def main():
    for _ in rir():
        a, b = mir()
        s = input()
        print(solve(a, b, s) or -1)


if __name__ == "__main__":
    main()
