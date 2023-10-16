
# Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro: "))

if num1 <= num2:
    inicio = num1
    fin = num2
else:
    inicio = num2
    fin = num1


while inicio <= fin:
    if inicio != fin:
        print(inicio, end="-")
    else:
        print(inicio, end="")
    inicio += 1

print()
