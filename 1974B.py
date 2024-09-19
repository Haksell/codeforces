for _ in range(int(input())):
    input()
    s = input()
    unique = sorted(set(s))
    mapping = {c1: c2 for c1, c2 in zip(unique, unique[::-1])}
    print("".join(map(mapping.get, s)))
