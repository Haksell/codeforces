# ruff: noqa: E731, E741
a = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
n = int(input())
print("YES" if any(n % d == 0 for d in a) else "NO")
