# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if all(ai % a[0] == 0 for ai in a) else "NO")
