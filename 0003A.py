def parse_line():
    x, y = map(ord, input())
    x -= 97
    y -= 48
    return x, y


x1, y1 = parse_line()
x2, y2 = parse_line()
moves = []
while x1 != x2 or y1 != y2:
    move = ""
    if x1 < x2:
        move += "R"
        x1 += 1
    elif x1 > x2:
        move += "L"
        x1 -= 1
    if y1 < y2:
        move += "U"
        y1 += 1
    elif y1 > y2:
        move += "D"
        y1 -= 1
    moves.append(move)
print(len(moves))
for move in moves:
    print(move)
