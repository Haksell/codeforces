# ruff: noqa: E731, E741
for _ in range(int(input())):
    print(sum(a != b for a, b in zip(input(), "codeforces")))
