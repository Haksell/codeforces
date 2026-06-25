# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


pows = [1]
while pows[-1] <= 200_000:
    pows.append(pows[-1] * 3)


def solve():
    l, r = mir()
    res = 0
    for i, (p1, p2) in enumerate(zip(pows, pows[1:]), 1):
        if p1 > r:
            break
        if p2 <= l:
            continue
        if l >= p1:
            res += i
        p1 = max(p1, l)
        p2 = min(p2, r + 1)
        res += i * (p2 - p1)
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
