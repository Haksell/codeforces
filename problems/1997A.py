# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    i = next((i for i in range(1, len(s)) if s[i - 1] == s[i]), None)
    if i is None:
        print(s + ("b" if s[-1] == "a" else "a"))
    else:
        print(s[:i] + ("b" if s[i] == "a" else "a") + s[i:])
