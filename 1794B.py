for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] == 1:
        a[0] = 2
    for i in range(1, n):
        while a[i] == 1 or a[i] % a[i - 1] == 0:
            a[i] += 1
    print(*a)
