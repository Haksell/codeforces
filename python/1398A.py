# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a, b, *_, c = list(map(int, input().split()))
    if a + b <= c:
        print(1, 2, n)
    else:
        print(-1)
