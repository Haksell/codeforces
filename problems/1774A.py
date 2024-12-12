# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    ans = []
    minus = True
    for c in input()[1:]:
        if c == "1":
            ans.append("-" if minus else "+")
            minus = not minus
        else:
            ans.append("+")
    print("".join(ans))
