for _ in range(int(input())):
    n = int(input())
    print("YES" if n % 11 * 111 <= n else "NO")
