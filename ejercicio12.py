Barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
Precio = 3.49 
Descuento = 0.6
Coste = Barras * Precio * (1 - Descuento)
print("El coste de una barra fresca es " + str(Precio) + "€")
print("El descuento sobre una barra no fresca es " + str(Descuento * 100) + "%")
print("El coste final a pagar es " + str(round(Coste, 2)) + "€")
input()