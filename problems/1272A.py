from itertools import product


def distance(a, b, c):
    return abs(a - b) + abs(b - c) + abs(c - a)


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(
        min(
            distance(a + da, b + db, c + dc)
            for da, db, dc in product([-1, 0, 1], repeat=3)
        )
    )