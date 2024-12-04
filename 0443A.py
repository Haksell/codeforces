from string import ascii_lowercase as al

exec(";".join(f"{c} = {ord(c)}" for c in al))
print(len(eval(input())))
