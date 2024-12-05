# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("PEAK" if a < b > c else "STAIR" if a < b < c else "NONE")
