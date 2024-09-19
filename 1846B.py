def solve(grid, c):
    return (
        grid[0][0] == grid[1][1] == grid[2][2] == c
        or grid[0][2] == grid[1][1] == grid[2][0] == c
        or any(row[0] == row[1] == row[2] == c for row in grid)
        or any(col[0] == col[1] == col[2] == c for col in zip(*grid))
    )


for _ in range(int(input())):
    grid = [input() for _ in range(3)]
    for c in "XO+":
        if solve(grid, c):
            print(c)
            break
    else:
        print("DRAW")
