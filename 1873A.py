# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print("NO" if s == "bca" or s == "cab" else "YES")
