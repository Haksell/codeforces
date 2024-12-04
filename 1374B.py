for _ in range(int(input())):
    n = int(input())
    two = 0
    while n & 1 == 0:
        two += 1
        n >>= 1
    three = 0
    while n % 3 == 0:
        three += 1
        n //= 3
    if n == 1 and three >= two:
        print(2 * three - two)
    else:
        print(-1)
