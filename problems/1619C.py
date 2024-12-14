# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a, s):
    a = list(map(int, a))[::-1]
    s = list(map(int, s))[::-1]
    res = []
    i = 0
    for c in a:
        if i == len(s):
            return None
        elif c <= s[i]:
            res.append(s[i] - c)
            i += 1
        elif i == len(s) - 1 or s[i + 1] != 1:
            return None
        else:
            res.append(s[i] - c + 10)
            i += 2
    res.extend(s[i:])
    return res


def main():
    for _ in rir():
        a, s = input().split()
        res = solve(a, s)
        if not res:
            print(-1)
            continue
        n = 0
        for d in reversed(res):
            n = 10 * n + d
        print(n)


if __name__ == "__main__":
    main()
