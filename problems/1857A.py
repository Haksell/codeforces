# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    print("NO" if sum(map(int, input().split())) & 1 else "YES")
