for _ in range(int(input())):
    n = int(input())
    s = n // 7 * 7
    print(s if s // 10 == n // 10 else s + 7)
