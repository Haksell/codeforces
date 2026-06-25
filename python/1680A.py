# ruff: noqa: E731, E741
for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    if r1 < l2 or r2 < l1:
        print(l1 + l2)
    else:
        print(max(l1, l2))
