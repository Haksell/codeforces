# ruff: noqa: E731, E741
def solve(s, t):
    s = list(s)
    ti = 0
    for si, c in enumerate(s):
        if c == t[ti]:
            ti += 1
        elif c == "?":
            s[si] = t[ti]
            ti += 1
        if ti == len(t):
            return "".join(s).replace("?", "z")


for _ in range(int(input())):
    s = input()
    t = input()
    res = solve(s, t)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(res)
