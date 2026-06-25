# ruff: noqa: E731, E741
def roll(h):
    i = next((i for i, (l, r) in enumerate(zip(h, h[1:])) if l < r), -1)
    if i != -1:
        h[i] += 1
    return i


for _ in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    if k >= n * max(h):
        print(-1)
        continue
    for _ in range(k):
        ans = roll(h)
        if ans == -1:
            print(-1)
            break
    else:
        print(ans + 1)
