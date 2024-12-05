# ruff: noqa: E731, E741
LIM = 50_001

for _ in range(int(input())):
    m = int(input())
    lst = [set(map(int, input().split())) for _ in range(2 * m)][1::2][::-1]
    ans = [lst[0].pop()]
    seen = set(ans)
    for a, b in zip(lst, lst[1:]):
        seen |= a
        ba = b - seen
        if not ba:
            ans = [-1]
            break
        x = ba.pop()
        ans.append(x)
        seen.add(x)
    print(*reversed(ans))
