# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = [input() for _ in range(n)]
    s = set(a)
    ans = []
    for w in a:
        for i in range(1, len(w)):
            if w[:i] in s and w[i:] in s:
                ans.append("1")
                break
        else:
            ans.append("0")
    print("".join(ans))
