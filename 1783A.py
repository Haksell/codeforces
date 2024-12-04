for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == 1:
        print("NO")
    else:
        print("YES")
        a = sorted(a)
        maxi = a.pop()
        print(maxi, *a)
