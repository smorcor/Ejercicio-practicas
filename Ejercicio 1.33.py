
# Ejercicio 1.33 - Lee 3 números y dame los números ordenados de menor a mayor.

n1 = float(input("Dame el primer número: "))
n2 = float(input("Dame el segundo número: "))
n3 = float(input("Dame el tercer número: "))

if (n1 < n2 and n1 < n3) :
    if n2<n3 : 
        print(n1 , " " , n2 , " " , n3)
    else :
        print(n1 , " " , n3 , " " , n2)
else :
    if (n2<n1 and n2<n3) :
        if n1<n3 :
            print(n2 , " " , n1 , " " , n3)
        else :
            print(n2 , " " , n3 , " " , n1)
    else :
        if (n3<n1 and n3<n2) :
            if (n1<n2) :
                print(n3 , " " , n1 , " " , n2)
            else :
                print(n3 , " " , n2 , " " , n1)