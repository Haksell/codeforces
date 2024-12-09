# ruff: noqa: E731, E741
def solve(n, a):
    ans = []
    i = 0
    while i < n:
        if a[i] == 0:
            ans.append(0)
        elif i + 1 < n and a[i + 1] == 1:
            ans.append(1)
            ans.append(1)
            i += 1
        elif i + 2 < n and a[i + 2] == 1:
            ans.append(1)
            ans.append(1)
            i += 2
        i += 1
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(len(ans))
    print(*ans)
