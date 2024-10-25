for _ in range(int(input())):
    n = int(input())
    res = list(map(int, input().split()))
    for i in range(1, n):
        if res[i] and res[i] <= res[i - 1]:
            print(-1)
            break
        res[i] += res[i - 1]
    else:
        print(*res)
