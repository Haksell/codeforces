for _ in range(int(input())):
    digits = list(map(int, input()))
    carry = False
    for i, d in reversed(list(enumerate(digits))):
        d += carry
        if d >= 5:
            digits[i] = -1
            carry = True
        else:
            digits[i] = d
            carry = False
    if carry:
        digits.insert(0, 1)
    try:
        i = digits.index(-1)
        print("".join(map(str, digits[:i])) + "0" * (len(digits) - i))
    except ValueError:
        print("".join(map(str, digits)))
