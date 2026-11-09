for _ in range(int(input())):
    print(*reversed([input().index("#") + 1 for _ in range(int(input()))]))
