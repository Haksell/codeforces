# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print(a + c if a + c <= b else a + b + c >> 1)
