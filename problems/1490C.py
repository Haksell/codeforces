# ruff: noqa: E731, E741
c = [i**3 for i in range(1, 10**4)]
s = set(c)
for _ in range(int(input())):
    n = int(input())
    for x in c:
        if n - x in s:
            print("YES")
            break
    else:
        print("NO")
