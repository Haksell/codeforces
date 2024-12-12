# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i, ai in enumerate(reversed(a)):
        if ai in s:
            print(n - i)
            break
        s.add(ai)
    else:
        print(0)
