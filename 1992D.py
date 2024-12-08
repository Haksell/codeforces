# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, m, k, a):
    a = ["L", *a, "L"]
    i = 0
    while i < len(a) - 1:
        if a[i] == "C":
            return False
        elif a[i] == "W":
            i += 1
            if k == 0:
                return False
            k -= 1
        else:
            for j in range(1, m + 1):
                if a[i + j] == "L":
                    i += j
                    break
            else:
                i += m
    return True


def main():
    for _ in rir():
        n, m, k = mir()
        a = input()
        print("YES" if solve(n, m, k, a) else "NO")


if __name__ == "__main__":
    main()
