# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    s = input()
    print(sum(a != b for a, b in zip(s, sorted(s))))
