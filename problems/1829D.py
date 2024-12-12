# ruff: noqa: E731, E741
from heapq import heappop, heappush


def solve(start, end):
    h = [start]
    seen = set()
    while h:
        n = heappop(h)
        if n == end:
            return True
        if n < end or n in seen:
            continue
        seen.add(n)
        third, remainder = divmod(n, 3)
        if remainder == 0:
            heappush(h, third)
            heappush(h, third << 1)
    return False


for _ in range(int(input())):
    start, end = map(int, input().split())
    print("YES" if solve(start, end) else "NO")
