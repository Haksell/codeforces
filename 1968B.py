for _ in range(int(input())):
    input()
    a = input()
    b = input()
    res = 0
    for bi in b:
        if bi == a[res]:
            res += 1
            if res == len(a):
                break
    print(res)
