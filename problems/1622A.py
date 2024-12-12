# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print(
        "YES" if a == b and c & 1 == 0 or c == b and a & 1 == 0 or a + b == c else "NO"
    )
