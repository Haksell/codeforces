# ruff: noqa: E731, E741
for _ in range(int(input())):
    l1, _, l2, _ = map(int, input().split())
    print(l1, l2 + (l1 == l2))
