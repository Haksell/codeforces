# ruff: noqa: E731, E741
for _ in range(int(input())):
    l = list(map(int, input().split()))
    b = sum(n & 1 for n in l)
    print("No" if b == 2 or (0 in l[:3] and b >= 2) else "Yes")
