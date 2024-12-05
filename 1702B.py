# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    cur = set()
    res = 0
    for c in s:
        if c not in cur:
            if len(cur) == 3:
                res += 1
                cur = {c}
            else:
                cur.add(c)
    res += bool(cur)
    print(res)
