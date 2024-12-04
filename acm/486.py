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
    s1 = input()
    s2 = input()
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    bulls = sum(map(str.__eq__, s1, s2))
    cows = sum(min(cnt1[c], cnt2[c]) for c in s1) - bulls
    print(bulls, cows)


if __name__ == "__main__":
    main()
