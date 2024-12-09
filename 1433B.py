# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    s = input()
    print(s[s.index("1") : s.rindex("1") : 2].count("0"))
