# ruff: noqa: E731, E741
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        h = []
        res = 0
        for card in mir():
            if card > 0:
                heappush(h, -card)
            elif h:
                res += -heappop(h)
        print(res)


if __name__ == "__main__":
    main()
