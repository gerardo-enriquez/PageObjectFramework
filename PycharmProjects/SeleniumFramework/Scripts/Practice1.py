def print_formatted(number):
    length = len(str(bin(number)[2::]))
    for i in range(1,number+1):
        deci = i
        octal = oct(i)[2::]
        hexa = hex(i)[2::]
        bina = bin(i)[2::]
        deci = str(deci)
        octal = str(octal)
        hexa = str(hexa).upper()
        bina = str(bina)
        print(deci.rjust(length) + octal.rjust(length+1) + hexa.rjust(length+1) + bina.rjust(length+1))


print_formatted(99)
