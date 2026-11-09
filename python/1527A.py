for _ in range(int(input())):
    print(~-(1 << ~-int(input()).bit_length()))
