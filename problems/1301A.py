# ruff: noqa: E731, E741
for _ in range(int(input())):
    print(
        "YES"
        if all(ai == ci or bi == ci for ai, bi, ci in zip(input(), input(), input()))
        else "NO"
    )
