from itertools import accumulate

for _ in range(int(input())):
    n, c = map(int, input().split())
    a = map(int, input().split())
    true_costs = sorted(i + ai + 1 for i, ai in enumerate(a))
    print(sum(1 for acc in accumulate(true_costs) if acc <= c))
