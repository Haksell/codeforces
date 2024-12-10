# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, _ = map(int, input().split())
    print(sum(input()[-1] == "R" for _ in range(h - 1)) + input().count("D"))
