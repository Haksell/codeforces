# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n % 5 == 0:
        ans += 1
        n = 4 * n // 5
    while n % 3 == 0:
        ans += 1
        n = 2 * n // 3
    while n & 1 == 0:
        ans += 1
        n >>= 1
    print(ans if n == 1 else -1)
