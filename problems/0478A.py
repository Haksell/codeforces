# ruff: noqa: E731, E741
q, r = divmod(sum(map(int, input().split())), 5)
print(q if r == 0 and q > 0 else -1)
