# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a, b):
    s = a[0]
    e = a[-1]
    if b[0] != s or b[-1] != e:
        return False
    if s == e:
        return True
    n = len(a)
    for i in range(n - 1):
        if a[i] == b[i] == s and a[i + 1] == b[i + 1] == e:
            return True
    return False


def main():
    for _ in rir():
        a = input()
        b = input()
        print("YES" if solve(a, b) else "NO")


if __name__ == "__main__":
    main()
