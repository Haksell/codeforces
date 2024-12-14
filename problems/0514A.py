# ruff: noqa: E731, E741
digits = list(map(int, input()))
print(
    *[d if d <= 4 or i == 0 and d == 9 else 9 - d for i, d in enumerate(digits)], sep=""
)
