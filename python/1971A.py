# ruff: noqa: E731, E741
for _ in range(int(input())):
    print(*sorted(map(int, input().split())))
