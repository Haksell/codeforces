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
        _, k = mir()
        a = lmir()
        cnt = Counter(a)
        for x in a:
            y = x - k
            if cnt[y] >= 2 or (cnt[y] >= 1 and x != y):
                print("YES")
                break
        else:
            print("NO")


"""
-2-2-2-2
-4-4-4 +2+2+2
-2-2 +4+4
"""


if __name__ == "__main__":
    main()
