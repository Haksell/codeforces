from itertools import takewhile


for _ in range(int(input())):
    s = input()
    t = input()
    print(
        len(s)
        + len(t)
        - max(
            0,
            sum(
                1
                for _ in takewhile(
                    lambda x: x[0] == x[1],
                    zip(s, t),
                )
            )
            - 1,
        ),
    )
