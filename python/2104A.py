# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    a, b, c = mir()
    q, r = divmod(a + b + c, 3)
    print("YES" if r == 0 and a <= q and b <= q else "NO")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
