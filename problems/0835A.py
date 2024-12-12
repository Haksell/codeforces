# ruff: noqa: E731, E741
s, v1, v2, p1, p2 = map(int, input().split())
t1 = v1 * s + 2 * p1
t2 = v2 * s + 2 * p2
print("First" if t1 < t2 else "Second" if t2 < t1 else "Friendship")
