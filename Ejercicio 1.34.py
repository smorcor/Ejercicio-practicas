
# Ejercicio 1.34 - Crea un algoritmo que asigne a una variable el número 3 y después pida un número. Debéis mostrar una serie de 3 en 3 tantos números cómo se hayan leído.

num = 3
serie = int(input("Dime cuantos números debe tener la serie: "))
cont = 1 
print(num)
while cont <= serie :
    if cont<serie : 
        num=num+3
        cont=cont+1
        print(num)
