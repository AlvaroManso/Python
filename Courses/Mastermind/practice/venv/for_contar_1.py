texto = input("escribe una frase: ")
espacios_cuantos = 0
puntos_cuantos = 0
comas_cuantos = 0
simbolo = (" ", ",", ".")
#simbolo1 = (" ")
#simbolo2 = (",")
#simbolo3 = (".")

for letras in texto:
    if letras in simbolo:
        espacios_cuantos += 1

    if letras in simbolo:
        puntos_cuantos += 1

    if letras in simbolo:
        comas_cuantos += 1


print("Espacios: {}" .format(espacios_cuantos))

print("comas: {}".format(comas_cuantos))

print("puntos: {}".format(puntos_cuantos))

