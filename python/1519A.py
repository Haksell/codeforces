# ruff: noqa: E731, E741
for _ in range(int(input())):
    r, b, d = map(int, input().split())
    if d == 0:
        print("YES" if r == b else "NO")
    else:
        bags = -(-abs(r - b) // d)
        print("YES" if bags <= min(r, b) else "NO")
