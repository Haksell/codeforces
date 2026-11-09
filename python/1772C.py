for _ in range(int(input())):
    k, n = map(int, input().split())
    arr = [1]
    for i in range(1, k):
        arr.append(min(arr[-1] + i, n + i + 1 - k))
    print(*arr)
