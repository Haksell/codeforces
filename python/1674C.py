# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = len(input())
    t = input()
    if t == "a":
        print(1)
    elif "a" in t:
        print(-1)
    else:
        print(1 << n)
