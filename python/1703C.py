# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        _, s = input().split()
        a[i] = (a[i] - s.count("U") + s.count("D")) % 10
    print(*a)
