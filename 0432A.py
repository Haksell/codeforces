# ruff: noqa: E731, E741
n, k = map(int, input().split())
y = list(map(int, input().split()))
can_participate = sum(5 - k >= x for x in y)
print(can_participate // 3)
