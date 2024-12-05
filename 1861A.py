# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print(13 if s.index("1") < s.index("3") else 31)
