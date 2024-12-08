# ruff: noqa: E731, E741
for _ in range(int(input())):
    print(int(input()) - sum(r == "2" for r in input().split()))
