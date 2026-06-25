# ruff: noqa: E731, E741
print(*[eval(input().replace(" ", "+")) for _ in range(int(input()))], sep="\n")
