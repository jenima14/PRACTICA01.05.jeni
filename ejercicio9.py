cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
input()