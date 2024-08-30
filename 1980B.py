for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    fav = a[f - 1]
    a.sort(reverse=True)
    x = a[k - 1]
    y = a[k] if k != n else None
    print("MAYBE" if x == y == fav else "YES" if x <= fav else "NO")
