for _ in range(int(input())):
    n = int(input())
    perms = [list(map(int, input().split())) for _ in range(n)]
    first = (
        perms[0][0]
        if perms[0][0] == perms[1][0] or perms[0][0] == perms[2][0]
        else perms[1][0]
    )
    for perm in perms:
        if perm[0] != first:
            print(first, *perm)
            break
