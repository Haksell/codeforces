# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    o = sum(x & 1 for x in a)
    print("Yes" if o == n else "No")
