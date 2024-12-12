# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    if k << 1 > n + 1:
        print(-1)
    else:
        for i in range(n):
            if i & 1 == 0 and i < k << 1:
                print("".join("R" if i == j else "." for j in range(n)))
            else:
                print("." * n)
