'''
Crear un programa que pida dos numeros
y obtenga coomo resultado cual de ellos es par
o si ambos lo son.
#Si ambos son pares, mostrar el mensaje "Ambos son pares"

'''
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))

if ((n1%2 ==0)) and ((n2%2 == 0)):
	print("Ambos son pares")
elif (n1%2 == 0) and (n2%2 != 0):
    print(f"El primer número {n1} es par")
    print(f"El segundo número {n2} es impar")
elif (n1%2 != 0) and (n2%2 == 0):
    print(f"El primer número {n1} es impar")
    print(f"El segundo número {n2} es par")
else:
     print("Los dos numeros son impares")