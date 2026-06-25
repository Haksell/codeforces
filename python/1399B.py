# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    candies = min(a)
    oranges = min(b)
    print(sum(max(c - candies, o - oranges) for c, o in zip(a, b)))
