# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print(
        "YES"
        if s.startswith("10") and len(s) >= 3 and s[2] != "0" and int(s[2:]) >= 2
        else "NO"
    )
