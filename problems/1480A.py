# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print(
        "".join(
            ("y" if c == "z" else "z") if i & 1 else ("b" if c == "a" else "a")
            for i, c in enumerate(s)
        )
    )
