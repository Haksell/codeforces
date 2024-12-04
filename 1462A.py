for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    left = 0
    right = n - 1
    a = []
    is_left = True
    while left <= right:
        if is_left:
            a.append(b[left])
            left += 1
        else:
            a.append(b[right])
            right -= 1
        is_left = not is_left
    print(*a)
