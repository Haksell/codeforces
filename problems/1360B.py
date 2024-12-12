# ruff: noqa: E731, E741
for _ in range(int(input())):
    a = int(input())
    nums = sorted([int(n) for n in input().split()])
    print(min(b - a for a, b in zip(nums[:-1], nums[1:])))
