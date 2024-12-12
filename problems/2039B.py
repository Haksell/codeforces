# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(s):
    if len(s) == 1:
        return -1
    if len(s) == 2:
        return s if s[0] == s[1] else -1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return s[i] * 2
    for a, b, c in zip(s, s[1:], s[2:]):
        if a != c:
            return a + b + c
    return -1


def main():
    for _ in rir():
        s = input()
        print(solve(s))


"""
abc 6
aba 5
abab 7
ababa 9
"""

"""
8
a
aa
aaa
aaaa
ab
aba
abab
ababa
"""

if __name__ == "__main__":
    main()
