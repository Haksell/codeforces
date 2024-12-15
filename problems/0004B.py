# ruff: noqa: E731, E741
from operator import itemgetter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    d, st = mir()
    lst = [lmir() for _ in range(d)]
    mini = sum(map(itemgetter(0), lst))
    maxi = sum(map(itemgetter(1), lst))
    if mini <= st <= maxi:
        print("YES")
        ans = []
        diff = st - mini
        for a, b in lst:
            nxt = min(a + diff, b)
            ans.append(nxt)
            diff -= nxt - a
        print(*ans)
    else:
        print("NO")


if __name__ == "__main__":
    main()
