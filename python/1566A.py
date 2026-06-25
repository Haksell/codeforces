# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, s = map(int, input().split())
    print(s // -~(n >> 1))
