# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    is_unique = all(si == s[0] for si in s)
    if not is_unique:
        a0 = next(i for i in range(n) if s[i] == "0")
        a1 = next(i for i in range(n) if s[i] == "1")
        z0 = next(i for i in reversed(range(n)) if s[i] == "0")
        z1 = next(i for i in reversed(range(n)) if s[i] == "1")
    for _ in range(q):
        l, r = [int(x) - 1 for x in input().split()]
        if is_unique:
            print("YES" if l != 0 or r != n - 1 else "NO")
        else:
            print(
                "YES"
                if (s[l] == "0" and l > a0)
                or (s[l] == "1" and l > a1)
                or (s[r] == "0" and r < z0)
                or (s[r] == "1" and r < z1)
                else "NO"
            )
