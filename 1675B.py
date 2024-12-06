# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    last = a[-1]
    ans = 0
    for n in a[-2::-1]:
        if last == 0:
            print(-1)
            break
        while n >= last:
            n >>= 1
            ans += 1
        last = n
    else:
        print(ans)
