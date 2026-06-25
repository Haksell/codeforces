# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if b + b - c >= a and (b + b - c) % a == 0:
        print("YES")
    elif (c + a) % (2 * b) == 0:
        print("YES")
    elif b + b - a >= c and (b + b - a) % c == 0:
        print("YES")
    else:
        print("NO")
