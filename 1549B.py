# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    opp = {i for i, c in enumerate(input()) if c == "1"}
    ans = 0
    for i, c in enumerate(input()):
        if c == "0":
            continue
        elif i - 1 in opp:
            opp.remove(i - 1)
            ans += 1
        elif i not in opp:
            ans += 1
        elif i + 1 in opp:
            opp.remove(i + 1)
            ans += 1
    print(ans)
