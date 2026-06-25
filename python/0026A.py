# ruff: noqa: E731, E741
size = int(input()) + 1
sieve = [0] * size
for i in range(2, size):
    if sieve[i] == 0:
        for j in range(i, size, i):
            sieve[j] += 1
print(sieve.count(2))
