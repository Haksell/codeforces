# ruff: noqa: E731, E741
res = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    res += a + 2 <= b
print(res)
