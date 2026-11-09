for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    if any(ai < 0 for ai in a):
        print("NO")
    else:
        print("YES")
        size = max(a) + 1
        print(size)
        print(*range(size))
