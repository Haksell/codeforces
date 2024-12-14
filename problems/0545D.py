# ruff: noqa: E731, E741
input()
a = list(map(int, input().split()))
wait = 0
ans = 0
for n in sorted(a):
    if n >= wait:
        ans += 1
        wait += n
print(ans)
