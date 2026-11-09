for _ in range(int(input())):
    x = input()
    d = int(x[0])
    n = len(x)
    before = 10 * (d - 1)
    after = n * (n + 1) // 2
    print(before + after)
