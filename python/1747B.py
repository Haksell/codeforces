# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    ans = n + 1 >> 1
    print(ans)
    for i in range(ans):
        print(3 * i + 1, 3 * (n - i))
