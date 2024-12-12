# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input()) >> 1
    print(n * (n + 1) * (2 * n + 1) // 3 << 2)
