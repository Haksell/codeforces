for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    print(m + max(i // 2 + (n - i + 1) // 2 for i, ai in enumerate(a) if ai == m))
