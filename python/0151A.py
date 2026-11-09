friends, k, m, c, d, salt, nl, np = map(int, input().split())
drink_portions = m * k // nl
lime_portions = c * d
salt_portions = salt // np
toasts = min(drink_portions, lime_portions, salt_portions)
print(toasts // friends)
