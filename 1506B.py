# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    stars = [i for i, c in enumerate(s) if c == "*"]
    if len(stars) == 1:  # TODO useful?
        print(1)
        continue
    ans = 1
    last = stars[0]
    for i in range(1, len(stars)):
        if i == len(stars) - 1 or (stars[i + 1] - last > k):
            ans += 1
            last = stars[i]
    print(ans)
