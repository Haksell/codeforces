# ruff: noqa: E731, E741
n = int(input())
days = list(map(int, input().split()))
n = (n - 1) % sum(days) + 1
for day, pages in enumerate(days, 1):
    if pages >= n:
        print(day)
        break
    n -= pages
