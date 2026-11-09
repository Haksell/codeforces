for _ in range(int(input())):
    size = int(input())
    grid = [input() for _ in range(size)]
    ones = [(y, x) for y in range(size) for x in range(size) if grid[y][x] == "1"]
    for y, x in ones:
        if not (
            y == size - 1
            or x == size - 1
            or grid[y][x + 1] == "1"
            or grid[y + 1][x] == "1"
        ):
            print("NO")
            break
    else:
        print("YES")
