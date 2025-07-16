'''
Ejemplo estructura de control for en Python
'''

#Ejemplo en C++
# for (int i = 0; i < 10; i++) {
# cout << ''El valor de i es: '' <<i << endl;
# }
#contador = 10
#for in range(0, contador):
#   print('El valor de i es:', i) #Imprimir el valor de i
#print('Fin del bucle for')  # Mensaje al finalizar el bucle

#Ejemplo con una lista
array = ['Auto',3, 4, 5, 'Avión', 'Barco']
print (len(array))      #Imprimir la longitud de la lista
array.append('Bicicleta')  # Añadir un elemento al final de la lista
print(array)  # Imprimir la lista actualizada
for i in range(len(array)):
    print('El valor del array es:', array[i])
print('Fin del bucle for con lista')  # Mensaje al finalizar el bucle
