def f(n):
    for i in range(n):
        for j in range(i + 1, n):
            if n & 1 == 0 and i & 1 == 0 and j == i + 1:
                yield 0
            elif (j - i - 1) & 1:
                yield -1
            else:
                yield 1


for _ in range(int(input())):
    n = int(input())
    print(*f(n))
