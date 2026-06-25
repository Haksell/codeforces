# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    x = next((x for x in map(int, input().split()) if x in a), 0)
    if x:
        print("YES")
        print(1, x)
    else:
        print("NO")
