# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    print("Alice" if (a ^ b) & 1 else "Bob")
