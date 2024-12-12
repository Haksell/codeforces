# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n & 1:
        print("NO")
    else:
        print("YES")
        print("B".join(["AA"] * (n >> 1)))
