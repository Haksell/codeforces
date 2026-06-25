# ruff: noqa: E731, E741
table = input()
hand = input().split()
print(
    "YES" if any(table[0] == card[0] or table[1] == card[1] for card in hand) else "NO"
)
