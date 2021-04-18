from random import randint


VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
TAMAÑO_BARRA_DE_VIDA = 10

while vida_pikachu > 0 and vida_squirtle > 0:

    print("turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltia")
        vida_squirtle -= 10
    else:
        print("pikachu ataca con onda trueno")
        vida_squirtle -= 11

    barras_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)

    print("Squirtle: ({}{})({}/{})".format("*" * barras_vida_squirtle, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_squirtle),
                                           vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    barras_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)

    print("Pikachu: ({}{})({}/{})".format("*" * barras_vida_pikachu, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU))

    print("turno squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle !="A" and ataque_squirtle != "B":
        ataque_squirtle = input("que ataque realizaras Placaje, Pistola Agua, Burbuja ")

    if ataque_squirtle == "P":
            print("Placaje")
            vida_pikachu -= 10
    elif ataque_squirtle == "A":
            print("Pistola Agua")
            vida_pikachu -= 11
    elif ataque_squirtle == "B":
            print("Burbuja")
            vida_pikachu -= 9

    print("Squirtle: ({}{})({}/{})".format("*" * barras_vida_squirtle,
                                           " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_squirtle),
                                           vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    print("Pikachu: ({}{})({}/{})".format("*" * barras_vida_pikachu, " " * (TAMAÑO_BARRA_DE_VIDA - barras_vida_pikachu),
                                          vida_pikachu, VIDA_INICIAL_PIKACHU))

if vida_pikachu > vida_squirtle:
        print("pikachu gana")
else:
        print("squirtle gana")