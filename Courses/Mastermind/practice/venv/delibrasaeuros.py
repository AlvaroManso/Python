dolar_euro = 0.84
libra_euro = 1.15
euro_libra = 0.87
euro_dolar = 1.19
resultado = 0

operacion = input("que operacion quieres hacer?\n"
                  "A de dolar a euro\n"
                  "B de euro a dolar\n"
                  "C de euro a libra\n"
                  "D de libra a euro\n")

cantidad = float(input("que cantidad deseas cambiar?"))

if operacion == "A":
    resultado = cantidad * dolar_euro
elif operacion == "B":
    resultado = cantidad * euro_dolar
elif operacion == "C":
    resultado = cantidad * euro_libra
elif operacion == "D":
    resultado = cantidad * libra_euro


print(resultado)