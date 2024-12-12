# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = []
    i = 2
    while len(a) < 2 and i * i < n:
        if n % i == 0:
            a.append(i)
            n //= i
        i += 1
    if len(a) == 2:
        print("YES")
        print(*a, n)
    else:
        print("NO")
