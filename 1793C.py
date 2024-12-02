# ruff: noqa: E731, E741
from collections import deque
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        l = lo = 1
        r = hi = ir()
        a = deque(mir())
        while a:
            if a[0] == lo:
                a.popleft()
                lo += 1
                l += 1
            elif a[0] == hi:
                a.popleft()
                l += 1
                hi -= 1
            elif a[-1] == lo:
                a.pop()
                lo += 1
                r -= 1
            elif a[-1] == hi:
                a.pop()
                r -= 1
                hi -= 1
            else:
                print(l, r)
                break
        else:
            print(-1)


if __name__ == "__main__":
    main()
