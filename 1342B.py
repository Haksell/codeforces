# ruff: noqa: E731, E741
for _ in range(int(input())):
    t = input()
    if len(set(t)) == 1:
        print(t)
    else:
        print("10" * len(t))
