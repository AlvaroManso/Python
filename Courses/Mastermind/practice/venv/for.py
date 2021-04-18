vocales = ["u", "a","i","e", "o"]
frase = "estoy estudiando uwu"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        print("he encontrado {}".format(letra))
        vocales_encontradas += 1

print("vocales encontradas: {}".format(vocales_encontradas))