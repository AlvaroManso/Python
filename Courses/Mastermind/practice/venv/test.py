titulo= "bienvenido al test"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("pregunta1\n"
               "a\n"
               "b\n"
               "c")
if opcion == "a":
    puntuacion += 0
elif opcion == "b":
    puntuacion += 5
elif opcion == "c":
    puntuacion += 10
else:
    print("las opciones son A, B o C")
    exit()

opcion = input("pregunta2\n"
               "a\n"
               "b\n"
               "c")
if opcion == "a":
    puntuacion += 0
elif opcion == "b":
    puntuacion += 5
elif opcion == "c":
    puntuacion += 10
else:
    print("las opciones son A, B o C")
    exit()

opcion = input("pregunta3\n"
               "a\n"
               "b\n"
               "c")
if opcion == "a":
    puntuacion += 0
elif opcion == "b":
    puntuacion += 5
elif opcion == "c":
    puntuacion += 10
else:
    print("las opciones son A, B o C")
    exit()

if puntuacion >= 25:
    print("gg")
elif puntuacion >= 15:
    print("gj")
else:
    print("FF")

print(puntuacion)