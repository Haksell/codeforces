# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(
        "YES"
        if len({n & 1 for n in a[::2]}) <= 1 and len({n & 1 for n in a[1::2]}) <= 1
        else "NO"
    )
