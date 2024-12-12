# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        d = Counter(mir())
        m = max(d.keys())
        for i in range(m):
            if d[i] < d[i + 1]:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
