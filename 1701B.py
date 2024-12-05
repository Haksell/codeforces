# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(2)
    remaining = set(range(1, n + 1))
    ans = []
    for i in range(1, n + 1, 2):
        while i <= n:
            ans.append(i)
            i <<= 1
    print(*ans)
