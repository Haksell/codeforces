# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(int(bool(sum(map(int, input().split())) % n)))
