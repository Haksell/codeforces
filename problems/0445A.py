# ruff: noqa: E731, E741
h, w = map(int, input().split())
for y in range(h):
    row = input()
    print(
        "".join(
            "-" if c == "-" else "W" if (y ^ x) & 1 else "B" for x, c in enumerate(row)
        )
    )
