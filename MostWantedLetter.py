def most_wanted_letter(entradaLetras):
    resultado = 0
    checked = "There are no letters in the string."
    check = any(c.isalpha() for c in entradaLetras)
    if check is False:
        return checked
    entradaLetras = entradaLetras.lower()
    for cadaLetra in entradaLetras:
        if cadaLetra.isalpha():
            if entradaLetras.count(cadaLetra) > resultado:
                laMasBuscado = cadaLetra
                resultado = entradaLetras.count(cadaLetra)
            elif entradaLetras.count(cadaLetra) == resultado:
                if cadaLetra < laMasBuscado:
                    laMasBuscado = cadaLetra
                    resultado = entradaLetras.count(cadaLetra)

    return laMasBuscado

print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))
