def int_ceil(num, den):
    return (num + den - 1) // den


for _ in range(int(input())):
    a, b, m = map(int, input().split())
    print(int_ceil(m + 1, a) + int_ceil(m + 1, b))
