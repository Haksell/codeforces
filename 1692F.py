# ruff: noqa: E731, E741
from itertools import combinations


def solve(last):
    if last[1] >= 3:
        return True
    for i, c in enumerate(last):
        j = (3 - 2 * i) % 10
        if i != j and c >= 2 and last[j]:
            return True
    for i, j in combinations(range(10), 2):
        k = (3 - i - j) % 10
        if k != i and k != j and last[i] and last[j] and last[k]:
            return True
    return False


for _ in range(int(input())):
    input()
    last = [0] * 10
    for x in input().split():
        last[int(x[-1])] += 1
    print("YES" if solve(last) else "NO")
