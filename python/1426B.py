# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(
        "YES"
        if any([input().split()[1] == input().split()[0] for _ in range(n)])
        and m & 1 == 0
        else "NO"
    )
