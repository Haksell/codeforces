for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print("NO")
    else:
        print("YES")
        o = n >> 1 if n & 1 else 1
        e = -o + 1 if n & 1 else -1
        print(*[o if i & 1 else e for i in range(n)])
