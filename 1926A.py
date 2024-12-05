# ruff: noqa: E731, E741
for _ in range(int(input())):
    print("A" if input().count("A") >= 3 else "B")
