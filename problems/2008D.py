# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    res = [0] * n
    p = [int(pi) - 1 for pi in read().split()]
    s = input()
    # cycles = []
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        cycle = [i]
        j = p[i]
        while i != j:
            cycle.append(j)
            j = p[j]
        # cycles.append(cycle)
        # print(cycle)
        black = sum(s[j] == "0" for j in cycle)
        for j in cycle:
            res[j] = black
        seen.update(cycle)
    print(*res)
