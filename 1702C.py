# ruff: noqa: E731, E741
import sys

EMPTY = 1
out = []
lines = [line.split() for line in sys.stdin.readlines()]
li = 1 + EMPTY
for _ in range(int(lines[0][0])):
    n, k = map(int, lines[li])
    u = lines[li + 1]
    first = dict()
    last = dict()
    for i, ui in enumerate(u):
        if ui not in first:
            first[ui] = i
        last[ui] = i
    for a, b in lines[li + 2 : li + 2 + k]:
        out.append("YES" if a in first and b in first and first[a] < last[b] else "NO")
    li += k + 2 + EMPTY
sys.stdout.write("\n".join(out))
