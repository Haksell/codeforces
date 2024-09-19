for _ in range(int(input())):
    n, k = map(int, input().split())
    two_by_two = ~-n << 2
    print((k + 1) >> 1 if k <= two_by_two else (two_by_two >> 1) + (k - two_by_two))

"""
n -> 2*n
2*n-1 -> 3*n-1
3*n-2 -> 4*n-2
"""
