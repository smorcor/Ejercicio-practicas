
# Ejercicio 1.31 - Lee un número hasta que el número esté en el rango 1-10

num = int(input("Introduce un número: "))
while (num < 1 or num > 10) :
    num = int(input("Inténtalo otra vez! (1-10): "))
print("Correcto!")