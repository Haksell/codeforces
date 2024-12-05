# ruff: noqa: E731, E741
for _ in range(int(input())):
    print("YES" if int(input()) == len(set(map(int, input().split()))) else "NO")
