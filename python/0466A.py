# ruff: noqa: E731, E741
def is_special_ticket_worth(m, a, b):
    return b / m < a


n, m, a, b = map(int, input().split())
if is_special_ticket_worth(m, a, b):
    floor_special = n // m
    ceil_special = -(-n // m)
    overflow = ceil_special * b
    just_right = floor_special * b + (n % m) * a
    print(min(just_right, overflow))
else:
    print(n * a)
