# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(a if 3 * a <= b else a + b >> 2)
