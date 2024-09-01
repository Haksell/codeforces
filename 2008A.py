import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()  # noqa: E731
ir = lambda: int(read())  # noqa: E731
rir = lambda: range(int(read()))  # noqa: E731
mir = lambda: map(int, read().split())  # noqa: E731
lmir = lambda: list(map(int, read().split()))  # noqa: E731

for _ in rir():
    a, b = mir()
    if a & 1:
        print("NO")
    elif a == 0:
        print("YES" if b & 1 == 0 else "NO")
    else:
        print("YES")
