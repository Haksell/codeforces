# ruff: noqa: E731, E741
from itertools import accumulate
from operator import itemgetter

MOD = 1_000_000_007
t, k = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(t)]
fibo = [1]
max_query = max(map(itemgetter(1), queries))
for i in range(1, max_query + 1):
    fibo.append((fibo[-1] + (fibo[-k] if k <= i else 0)) % MOD)
acc = list(accumulate(fibo))
for a, b in queries:
    print((acc[b] - acc[a - 1]) % MOD)
