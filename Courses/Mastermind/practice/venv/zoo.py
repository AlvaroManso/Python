edad = int(input("que edad tiene: "))
carnet = input("E / P / F / N")

if (25<= edad <= 35 and carnet == "E") or edad < 10 or (edad >= 65 and carnet == "P") or (carnet == "F"):
    print("se te aplica el descuento.")
else:
    print("no hay descuento para ti")