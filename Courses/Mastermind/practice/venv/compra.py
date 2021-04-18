lista = []
print("Programa lista de la compra\n")
articulo = input("que desea comprar? [Q] PARA SALIR")

while articulo != "Q":

    confirmacion = input("estas seguro?S/N")
    if confirmacion == "S":
        lista.append(articulo)
        print("{} fue añadido a la lista:".format(articulo))
        articulo = input("que desea comprar? [Q] PARA SALIR")
    elif confirmacion == "N":
        print("no se añadio")

if articulo == "Q":
    print(lista)
    exit("adios bro")


