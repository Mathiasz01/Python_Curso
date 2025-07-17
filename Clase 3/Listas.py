'''
Ejemplo de listas en Python
'''

array= [1, 2, 3, [2, 3, 4], True, False, "Hola", "Mundo"]
print(array)

# Acceso a elementos de la lista
#print(array[0])
#print(array[3])
print(array[0:3]) 
print(len(array))  # Longitud de la lista
array.append(101)  # Añadir un elemento al final de la lista
print(array)  
array.insert(1,5)# Insertar un elemento en una posición específica
array.remove(101)  # Eliminar un elemento específico
print(array)
array.pop(2)
print(array)  # Eliminar el elemento en la posición 2
array.clear()  # Limpiar la lista
print(array)  # Lista vacía
array = [1, 2, 3, [2, 3, 4], True, False, "Hola", "Mundo"]
array2 = [4, 5, 6]
array3 = array + array2  # Concatenar listas
print(array3)  # Imprimir la lista concatenada
print('3' in array2)
print('Hola' in array)
print(array.index("Hola"))  # Obtener el índice de un elemento
print(array.count(2))  # Contar cuántas veces aparece un elemento
array4 = (1, 2, 3, 4, 5, 6)
array4 = list(array4)  # Convertir la tupla a lista para poder invertirla
array4.reverse() # Invertir la tupla      
print(array4)  # Imprimir la tupla invertida
array5 = [1, 5, 3, 2, 4]  # Crear una lista desordenada
array5.sort()  # Ordenar la lista
print(array5)  # Imprimir la lista ordenada