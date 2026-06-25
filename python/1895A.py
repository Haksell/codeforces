# ruff: noqa: E731, E741
for _ in range(int(input())):
    chest, key, k = map(int, input().split())
    if key <= chest:
        print(chest)
    else:
        print(key + max(0, key - chest - k))
