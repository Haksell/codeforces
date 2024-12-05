# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    print(sum(min(n, s.count(c)) for c in "ABCD"))
