# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    max_a = max(map(int, input().split()))
    input()
    max_b = max(map(int, input().split()))
    print("Alice" if max_a >= max_b else "Bob")
    print("Alice" if max_a > max_b else "Bob")
