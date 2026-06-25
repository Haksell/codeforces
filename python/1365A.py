# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(
        "AVsihvieskh"[
            ~min(
                sum(all(x == 0 for x in r) for r in a),
                sum(all(x == 0 for x in c) for c in zip(*a)),
            )
            & 1 :: 2
        ]
    )
