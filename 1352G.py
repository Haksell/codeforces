for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print(-1)
        continue
    res = list(range((n - 1) | 1, 0, -2))
    res.append(4)
    res.append(2)
    res.extend(range(6, n + 1, 2))
    print(*res)
