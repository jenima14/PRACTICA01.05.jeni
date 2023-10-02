n = int(input("escribe un entero positivo: "))
if n <= 0:
    print("El número escrito no es positivo.")
else:
    suma = (n * (n + 1)) // 2
    print("La suma de los enteros positivos desde 1 hasta", n, "es:", suma)
    input()