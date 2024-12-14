# ruff: noqa: E731, E741
def triangle(n):
    return n * (n + 1) >> 1


s = input()
k = int(input())
w = list(map(int, input().split()))
print(
    sum(i * w[ord(si) - 97] for i, si in enumerate(s, 1))
    + ((triangle(k + len(s)) - triangle(len(s))) * max(w))
)
