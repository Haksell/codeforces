# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        s = sum(a)
        m, r = divmod(s, n)
        print("YES" if r == 0 and sum(a[1::2]) == n // 2 * m else "NO")


if __name__ == "__main__":
    main()
