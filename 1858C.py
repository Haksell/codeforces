for _ in range(int(input())):
    n = int(input())
    nums = set(range(1, n + 1))
    res = []
    for i in range(1, n + 1):
        while i <= n and i in nums:
            res.append(i)
            nums.discard(i)
            i <<= 1
    print(*res)
