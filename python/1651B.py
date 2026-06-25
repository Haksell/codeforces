# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n <= 19:
        print("YES")
        print(*[3**i for i in range(n)])
    else:
        print("NO")
