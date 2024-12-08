# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max(map(max, a, b)) * max(map(min, a, b)))
