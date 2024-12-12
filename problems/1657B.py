# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, B, x, y = map(int, input().split())
    ans = [0]
    for _ in range(n):
        add_x = ans[-1] + x
        ans.append(add_x if add_x <= B else ans[-1] - y)
    print(sum(ans))
