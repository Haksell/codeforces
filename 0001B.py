import re


def standard_to_excel(col):
    col = int(col)
    digits = []
    while col > 0:
        col, d = divmod(col - 1, 26)
        digits.append(chr(65 + d))
    return "".join(reversed(digits))


def excel_to_standard(col):
    res = 0
    for d in col:
        res = 26 * res + ord(d) - 64
    return res


for _ in range(int(input())):
    s = input()
    if re.fullmatch(r"R\d+C\d+", s):
        row, col = re.findall(r"\d+", s)
        print(f"{standard_to_excel(col)}{row}")
    else:
        col, row = re.fullmatch(r"([A-Z]+)(\d+)", s).groups()
        print(f"R{row}C{excel_to_standard(col)}")
