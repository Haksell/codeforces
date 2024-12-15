# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def make_lps(s):
    lps = [0] * len(s)
    length = 0
    i = 1
    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length == 0:
            i += 1
        else:
            length = lps[length - 1]
    return lps


def main():
    s = input()
    lps = make_lps(s)
    mid_prefix_lengths = set(lps[1:-1])
    length = lps[-1]
    while length > 0:
        if length in mid_prefix_lengths:
            print(s[:length])
            return
        length = lps[length - 1]
    print("Just a legend")


if __name__ == "__main__":
    main()
