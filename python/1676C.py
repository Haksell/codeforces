# ruff: noqa: E731, E741
def cost(s1, s2):
    return sum(abs(ord(c1) - ord(c2)) for c1, c2 in zip(s1, s2))


for _ in range(int(input())):
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    print(min(cost(s1, s2) for i, s1 in enumerate(a) for s2 in a[:i]))
