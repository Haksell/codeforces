# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, _ = mir()
    g = [lmir() for _ in range(n)]
    res = [-1] * n
    for i, cow in enumerate(g):
        nth = cow[0] % n
        if any(x % n != nth for x in cow[1:]):
            print(-1)
            return
        res[nth] = i + 1
    print(*res)


def main():
    for _ in rir():
        solve()


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
