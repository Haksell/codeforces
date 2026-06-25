# ruff: noqa: E731, E741
for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if h > c:
        hamburger = min(b >> 1, p)
        b -= hamburger << 1
        chicken = min(b >> 1, f)
    else:
        chicken = min(b >> 1, f)
        b -= chicken << 1
        hamburger = min(b >> 1, p)
    print(hamburger * h + chicken * c)
