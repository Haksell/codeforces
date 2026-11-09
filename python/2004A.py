for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    print("YES" if n == 2 and x[1] - x[0] > 1 else "NO")
