for _ in range(int(input())):
    n = input()
    print(n[1] if len(n) == 2 else min(n))
