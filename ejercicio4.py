#programa que identifica si el numero es negativo positivo o cero

n = int(input("Ingrese un numero: "))
if n > 0:
    print("El numero es positivo")
elif n < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")