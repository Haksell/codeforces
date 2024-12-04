for _ in range(int(input())):
    n = int(input())
    c1 = c2 = n // 3
    mod = n % 3
    if mod == 1:
        c1 += 1
    elif mod == 2:
        c2 += 1
    print(c1, c2)
