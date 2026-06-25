# ruff: noqa: E731, E741
n = int(input())
print(sum(n % i == 0 for i in range(1, n)))
