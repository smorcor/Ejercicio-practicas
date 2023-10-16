# Ejercicio 1.36 - Calcula la media de las notas de un curso.
# Píde el número de notas que va a introducir al principio.
# El número de notas no puede ser un número superior a 100, o inferior a 1.
# Si no introduce un número de notas correcto escribimos el mensaje "Error - el número de notas debe ser un número entero entre 1 y 100"

total = int(input("¿Cuántas notas vas a introducir? "))
while (total < 1 or total > 100) :
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    total = int(input("¿Cuántas notas vas a introducir? "))

print(f"Dame las {total} notas del curso:")

media = 0
cont = 0

while cont < total:
    nota = float(input())
    media += nota
    cont += 1

media = media / total

print(f"La media es {media:.2f}")