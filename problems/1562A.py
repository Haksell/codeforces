# ruff: noqa: E731, E741
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(r % max(l, r // 2 + 1))
