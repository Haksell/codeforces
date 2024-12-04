for _ in range(int(input())):
    n = int(input())
    if n % 4 != 0:
        print("NO")
    else:
        evens = range(2, n + 1, 2)
        odds = range(1, n - 2, 2)
        last_odd = n * 3 // 2 - 1
        print("YES")
        print(*evens, *odds, last_odd)
