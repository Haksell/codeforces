# ruff: noqa: E731, E741
def ispal(s):
    return all(s[i] == s[~i] for i in range(len(s) >> 1))


def g(s):
    t = "a" + s
    if not ispal(t):
        return f"YES\n{t}"
    t = s + "a"
    if not ispal(t):
        return f"YES\n{t}"
    return "NO"


for _ in range(int(input())):
    res = g(input())
    print(res)
