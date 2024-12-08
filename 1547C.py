# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    b = list(map(int, input().split()))[::-1]
    ans = []
    while a or b:
        ans.append(a.pop() if not b or (a and a[-1] < b[-1]) else b.pop())
    for x in ans:
        if x == 0:
            k += 1
        elif x > k:
            print(-1)
            break
    else:
        print(*ans)
