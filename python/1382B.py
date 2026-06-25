# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = next((i for i, x in enumerate(a) if x != 1), n)
    print("SFeicrosntd"[[~i, n][i == n] & 1 :: 2])
