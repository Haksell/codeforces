# ruff: noqa: E731, E741
for _ in range(int(input())):
    a = int(input())
    nu = sorted([int(n) for n in input().split()])
    od = sum(n % 2 for n in nu)
    if od % 2 == 0:
        print("YES")
    elif any(b - a == 1 for a, b in zip(nu, nu[1:])):
        print("YES")
    else:
        print("NO")
