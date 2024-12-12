for _ in range(int(input())):
    n = int(input())
    a = [int(x) - 1 for x in input().split()]
    cycle_lengths = [-1] * n
    for i, ai in enumerate(a):
        if cycle_lengths[i] != -1:
            continue
        cycle = [ai]
        while ai != i:
            ai = a[ai]
            cycle.append(ai)
        for ai in cycle:
            cycle_lengths[ai] = len(cycle)
    print(*cycle_lengths)