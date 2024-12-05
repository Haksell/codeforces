# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print("Bob" if n <= 4 else "Alice")
