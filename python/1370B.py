# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    even = []
    odd = []
    for i, x in enumerate(a, 1):
        (odd if x & 1 else even).append(i)
    if len(odd) & 1:
        odd.pop()
        even.pop()
    else:
        to_remove = odd if len(odd) >= 2 else even
        to_remove.pop()
        to_remove.pop()
    while odd:
        print(odd.pop(), odd.pop())
    while even:
        print(even.pop(), even.pop())
