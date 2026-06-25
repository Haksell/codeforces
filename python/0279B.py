# ruff: noqa: E731, E741
n, t = map(int, input().split())
a = list(map(int, input().split()))

maxi = curr = left = 0
right = -1
while right < n - 1:
    if curr + a[right + 1] <= t:
        curr += a[right + 1]
        right += 1
    else:
        curr -= a[left]
        left += 1
    maxi = max(maxi, right - left + 1)
print(maxi)
