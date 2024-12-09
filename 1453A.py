# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = set(map(int, input().split()))
    print(sum(int(x) in a for x in input().split()))
