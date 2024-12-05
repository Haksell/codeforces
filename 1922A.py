# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    print(
        "YES"
        if any(a != c and b != c for a, b, c in zip(input(), input(), input()))
        else "NO"
    )
