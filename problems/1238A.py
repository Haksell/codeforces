# ruff: noqa: E731, E741
for _ in range(int(input())):
    print("YNEOS"[eval(input().replace(" ", "-")) == 1 :: 2])
