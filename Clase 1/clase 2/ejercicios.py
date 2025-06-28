'''
Crear un programa que pida dos numeros
y obtenga coomo resultado cual de ellos es par
o si ambos lo son.
#Si ambos son pares, mostrar el mensaje "Ambos son pares"

'''
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))

if n1 % 2 == 0 and n2 % 2 == 0:
	print("Ambos son pares")