for _ in range(int(input())):
    n = int(input())
    if n < 7 or n == 9:
        print("NO")
    else:
        print("YES")
        if n % 3 == 0:
            print(1, 4, n - 5)
        else:
            print(1, 2, n - 3)
