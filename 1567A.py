# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    print(s.translate(str.maketrans("UD", "DU")))
