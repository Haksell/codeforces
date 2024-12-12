# ruff: noqa: E731, E741
k, r = map(int, input().split())
for i in range(1, 11):
    if k * i % 10 in [0, r]:
        print(i)
        exit()
