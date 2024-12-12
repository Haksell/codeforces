# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    p = [x - 1 for x in mir()]
    res = [-1] * n
    for i in range(n):
        if res[i] != -1:
            continue
        path = []
        seen = set()
        while i not in seen:
            path.append(i)
            seen.add(i)
            i = p[i]
        in_cycle = False
        for x in path:
            if x == i:
                in_cycle = True
            res[x] = x if in_cycle else i
    print(*[x + 1 for x in res])


if __name__ == "__main__":
    main()
