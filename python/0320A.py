# ruff: noqa: E731, E741
n = int(input())
while True:
    if n == 0:
        print("YES")
        break
    elif n % 1000 == 144:
        n //= 1000
    elif n % 100 == 14:
        n //= 100
    elif n % 10 == 1:
        n //= 10
    else:
        print("NO")
        break
