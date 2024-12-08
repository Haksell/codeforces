# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = nums = list(map(int, input().split()))
    size = abs(a - b) << 1
    print((c + (size >> 1) - 1) % size + 1 if max(nums) <= size else -1)
