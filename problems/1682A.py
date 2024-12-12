# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    h = n >> 1
    s = input()
    i = next((i for i in range(h + 1, n) if s[i] != s[h]), n)
    print(2 * i - n)
