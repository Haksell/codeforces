# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    s = set()
    for i, (ai, bi) in enumerate(
        zip(map(int, input().split()), map(int, input().split()))
    ):
        if (bi > ai and 1 not in s) or (bi < ai and -1 not in s):
            print("NO")
            break
        s.add(ai)
    else:
        print("YES")
