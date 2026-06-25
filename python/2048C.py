# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    s = input()
    n = len(s)
    z = s.find("0")
    if z == -1:
        print(1, n, 1, 1)
        return
    o = [i for i in range(z) if s[i] == "1"]
    size2 = len(s) - z
    for j in range(1, size2):
        if len(o) == 1:
            break
        good = any(s[oi + j] != s[z + j] for oi in o)
        if good:
            o = [oi for oi in o if s[oi + j] != s[z + j]]
    print(1, n, o[0] + 1, o[0] + size2)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
