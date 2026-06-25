# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    print(*sorted(map(int, input().split()), reverse=True))
