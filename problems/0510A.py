# ruff: noqa: E731, E741
h, w = map(int, input().split())
for i in range(h):
    print(["#" * w, "." * (w - 1) + "#", "#" * w, "#" + "." * (w - 1)][i & 3])
