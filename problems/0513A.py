# ruff: noqa: E731, E741
n1, n2, _, _ = map(int, input().split())
print("First" if n1 > n2 else "Second")
