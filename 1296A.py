# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("NO" if sum(a) % 2 == 0 and len({x & 1 for x in a}) == 1 else "YES")
