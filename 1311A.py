for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print(1 if (a ^ b) & 1 else 2)
    elif a > b:
        print(2 if (a ^ b) & 1 else 1)
    else:
        print(0)