# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def longest_increasing(a):
    res = (1, 1)
    prev = a[0]
    start = 0
    for i in range(1, len(a)):
        if a[i] < prev:
            if i - start > res[1] - res[0]:
                res = (start, i - 1)
            start = i
        prev = a[i]
    return res


def solve():
    n = ir()
    a1 = lmir()
    a2 = lmir()
    start = next((i for i in range(n) if a1[i] != a2[i]), None)
    if start is None:
        return longest_increasing(a1)
    end = next(i for i in reversed(range(n)) if a1[i] != a2[i])
    sub = a1[start : end + 1]
    mini = min(sub)
    while start >= 1 and a1[start - 1] <= mini:
        start -= 1
        mini = a1[start]
    maxi = max(sub)
    while end < n - 1 and a1[end + 1] >= maxi:
        end += 1
        maxi = a1[end]
    return (start + 1, end + 1)


def main():
    for _ in rir():
        print(*solve())


if __name__ == "__main__":
    main()
