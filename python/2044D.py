# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    a = lmir()
    seen = [False] * n
    for ai in a:
        seen[ai - 1] = True
    unseen = {i + 1 for i, s in enumerate(seen) if not s}
    seen = [False] * n
    res = []
    for ai in a:
        if seen[ai - 1]:
            res.append(unseen.pop())
        else:
            res.append(ai)
            seen[ai - 1] = True
    print(*res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
