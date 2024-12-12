# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(l, r):
    d = r - l
    if l & 1:
        d += 1
    return d + 1 >> 2


assert solve(1, 1) == 0
assert solve(1, 2) == 0
assert solve(1, 3) == 1
assert solve(1, 4) == 1
assert solve(1, 5) == 1
assert solve(1, 6) == 1
assert solve(1, 7) == 2
assert solve(1, 8) == 2
assert solve(1, 9) == 2

assert solve(2, 2) == 0
assert solve(2, 3) == 0
assert solve(2, 4) == 0
assert solve(2, 5) == 1
assert solve(2, 6) == 1
assert solve(2, 7) == 1
assert solve(2, 8) == 1
assert solve(2, 9) == 2

assert solve(3, 3) == 0
assert solve(3, 4) == 0
assert solve(3, 5) == 1
assert solve(3, 6) == 1
assert solve(3, 7) == 1
assert solve(3, 8) == 1
assert solve(3, 9) == 2

for _ in rir():
    l, r = mir()
    print(solve(l, r))
