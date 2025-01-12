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
    b = lmir()
    small = [i for i in range(n) if a[i] < b[i]]
    if len(small) == 0:
        return True
    if len(small) >= 2:
        return False
    i = small[0]
    d = b[i] - a[i]
    return all(ai - d >= bi for j, (ai, bi) in enumerate(zip(a, b)) if i != j)


def main():
    for _ in rir():
        print("YES" if solve() else "NO")


if __name__ == "__main__":
    main()
