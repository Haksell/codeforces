# ruff: noqa: E731, E741
for _ in range(int(input())):
    print("NO" if 360 % (180 - int(input())) else "YES")
