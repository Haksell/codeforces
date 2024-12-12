# ruff: noqa: E731, E741
for _ in range(int(input())):
    one, two = map(int, input().split())
    print(1 if one == 0 else one + 2 * two + 1)
