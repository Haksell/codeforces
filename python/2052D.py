# ruff: noqa: E731, E741
from heapq import heapify, heappop, heappush
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(cond, deps):
    set_idx = unset_idx = None
    for i, (is_set, is_true) in enumerate(cond):
        if is_true:
            if is_set:
                if set_idx is not None:
                    return
                set_idx = i
            else:
                if unset_idx:
                    return
                unset_idx = i

    if unset_idx is not None and set_idx is None:
        return
    if set_idx is not None and unset_idx is not None:
        deps.append((set_idx, unset_idx))

    for i, (is_set, is_true) in enumerate(cond):
        if is_set and not is_true:
            if set_idx is None:
                return
            deps.append((set_idx, i))
            if unset_idx is not None:
                deps.append((i, unset_idx))
        if set_idx is not None and unset_idx is None and not is_set and not is_true:
            deps.append((i, set_idx))

    n = len(cond)
    children = [set() for _ in range(n)]
    parents = [set() for _ in range(n)]
    for u, v in deps:
        parents[v].add(u)
        children[u].add(v)

    b = False
    tps = []
    heap = [
        (0 if not is_set and not is_true else 1, i)
        for i, (is_set, is_true) in enumerate(cond)
        if not parents[i]
    ]
    heapify(heap)
    while heap:
        (_, i) = heappop(heap)
        is_set, is_true = cond[i]

        if b and not is_set and not is_true:
            if unset_idx is None:
                return
            parents[i].add(unset_idx)
            children[unset_idx].add(i)
            continue

        tps.append(i)
        if is_set:
            if is_true:
                if b:
                    return
                b = True
            else:
                if not b:
                    return
        else:
            if is_true:
                if not b:
                    return
                b = False
            else:
                if b:
                    return

        for j in children[i]:
            parents[j].remove(i)
            if not parents[j]:
                is_set, is_true = cond[j]
                heappush(heap, (0 if not is_set and not is_true else 1, j))

    if len(tps) == n:
        return tps


def main():
    cond = []
    for _ in rir():
        a, b = input().split()
        is_set = a == "set"
        is_true = b == "true"
        cond.append((is_set, is_true))
    deps = []
    for _ in rir():
        a, b = mir()
        deps.append((a - 1, b - 1))
    res = solve(cond, deps)
    if res is None:
        print(-1)
    else:
        print(*[r + 1 for r in res])


if __name__ == "__main__":
    main()
