import random

print("la mazmorra del horror\n"
      "----------------------\n"
      "estas encerrado en Marte y tienes que escapar de esa prision \n"
      "tienes dos opciones para comenzar tu super escape, a la izq tienes la puerta de la celda semiabierta\n"
      "a la derecha tienes una escotilla en el suelo, que parece estar muy oxidada.\n"
      "que decides hacer\n")

n = random.randint(1, 100)
espada = False
opcion = input("quieres tomar la puerta(a) o la escotilla(b)?\n")
if opcion == "a":
    print("detras de la puerta hay otro guardian, que haces?\n")
    opcion = input("te haces el dormido(a) o sales corriendo hasta la siguiente puerta(b)\n")
    if opcion == "a":
        print("el guardia te atrapa y te encierra en una celda de maxima seguridad FIN del Juego Amigo\n")
    elif opcion == "b":
        print("llegas a una sala con un sapo gigante que te regala una espada\n")
        opcion = input ("aceptas?(a) si (b) no \n")
        if opcion == "a":
            espada = True
            print("bien, coges la espada pasas a la siguiente sala y ves dos caminos, cual eliges?\n")
            elif opcion == "b":
                print("la rana se enfada y te mata")
                exit()
    elif opcion = "b":
        print("ves 10 esqueltos, te tienes que pelear")
        if espada == True:
            print("los matas a todos")
            print("pasas a otra sala, te encuentras a un mago que te pregunta la respuesta de esta suma {}+10:".format(n))
            respuesta = int(input("que numero quieres"))
            if respuesta == n + 10:
                print("estas perra")
            elif respuesta != n + 10:
                print("pasa anda pasa con las putas")
                exit()
        elif espada == False:
            print("te matan a pedras")
            exit()