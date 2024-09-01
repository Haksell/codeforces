import math
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()  # noqa: E731
ir = lambda: int(read())  # noqa: E731
rir = lambda: range(int(read()))  # noqa: E731
mir = lambda: map(int, read().split())  # noqa: E731
lmir = lambda: list(map(int, read().split()))  # noqa: E731

for _ in rir():
    n = ir()
    s = input()
    i = math.isqrt(n)
    if i * i != n:
        print("No")
    elif i <= 2:
        print("Yes" if all(c == "1" for c in s) else "No")
    else:
        t = []
        for j in range(i):
            if j == 0 or j == i - 1:
                t.append("1" * i)
            else:
                t.append("1")
                t.append("0" * (i - 2))
                t.append("1")
        print("Yes" if s == "".join(t) else "No")
