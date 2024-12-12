# ruff: noqa: E731, E741
queries = [int(input()) for _ in range(int(input()))]

sum_digits = [0]
acc = [0]
for i in range(1, max(queries) + 1):
    divs = 0
    while i % 10 == 0:
        divs += 1
        i //= 10
    sd = sum_digits[-1] + 1 if divs == 0 else sum_digits[i]
    sum_digits.append(sd)
    acc.append(acc[-1] + sd)

for query in queries:
    print(acc[query])
