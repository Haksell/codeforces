# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    *a, last = map(int, input().split())
    print(max(a) + last)
