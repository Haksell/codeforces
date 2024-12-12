# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    left = [i + 1 for i, ai in enumerate(a) if ai]
    rm = len(left) - s
    if rm < 0:
        print(-1)
        continue
    right = [0] + [n - i + 1 for i in reversed(left)]
    left = [0] + left
    print(min(map(int.__add__, left[: rm + 1], right[rm::-1])))
