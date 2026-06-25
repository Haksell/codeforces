# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    print(max(max(0, x - i) for i, x in enumerate(map(int, input().split()), 1)))
