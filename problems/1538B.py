# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    q, r = divmod(sum(a), n)
    print(sum(c > q for c in a) if r == 0 else -1)
