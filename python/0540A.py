# ruff: noqa: E731, E741
input()
c1 = list(map(int, input()))
c2 = list(map(int, input()))
print(sum(min(abs(n1 - n2), 10 + n1 - n2, 10 + n2 - n1) for n1, n2 in zip(c1, c2)))
