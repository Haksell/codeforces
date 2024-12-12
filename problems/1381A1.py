# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    ans = []
    for i in range(n - 1, 0, -1):
        if a[i] != b[i]:
            if a[0] == b[i]:
                ans.append(1)
                a[0] = 1 - a[0]
            ans.append(i + 1)
            a[: i + 1] = [1 - x for x in a[i::-1]]
    if a[0] != b[0]:
        a[0] = 1 - a[0]
        ans.append(1)
    print(len(ans), *ans)
