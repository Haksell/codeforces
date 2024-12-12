# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = [0] * k
    for i, ai in enumerate(map(int, input().split())):
        ik = i % k
        ans[ik] = max(ans[ik], ai)
    print(sum(ans))
