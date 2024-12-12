# ruff: noqa: E731, E741
import sys

cin = sys.stdin
read = cin.readline
cout = sys.stdout
write = cout.write
rir = lambda: range(int(read()))
ir = lambda: int(read())
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    mines = []
    miners = []
    for _ in range(2 * n):
        x, y = mir()
        if y == 0:
            mines.append(abs(x))
        else:
            miners.append(abs(y))

    mines.sort()
    miners.sort()
    res = 0
    for _ in range(n):
        a, b = mines.pop(), miners.pop()
        res += (a * a + b * b) ** 0.5
    print(res)
