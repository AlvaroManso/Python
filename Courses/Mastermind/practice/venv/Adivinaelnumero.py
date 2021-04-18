import random

n = random.randint(1, 10)
numero_del_usuario = int(input("intenta adivinar el numero que estoy pensando, del 1 al 10 "))

if numero_del_usuario != n:
    print("Error, fallaste amigo")
if numero_del_usuario == n:
    print("enhorabuena amigo, has acertado")

if numero_del_usuario > 10:
    print("te has pasado xD")

if numero_del_usuario < 1:
    print("sube un poco amigo")
if numero_del_usuario == 666:
    print("bro, este es el numero de la bestia xDDD")

print("el numero ganador era {}".format(n))