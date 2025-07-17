'''
Ejemplo de funciones en Python
'''



# Funciones en C++
#include <iostream>
#  using namespace std;
#  void sumar(int a, int b) Prototipo de función

#int main() {
    #int a= 6, b=4
    #int rest=0 ;
    #rest = sumar(a, b);
    #cout <<''Resultado '' <<rest<< endl;  // llamada a la función
    #return 0;
#}

#void sumar(int a, int b) {
#    return a + b;  // Definición de la función
#}

def sumar(a, b):
    return a + b  # Definición de la función

a= 2
b= 7

resultado = sumar(a, b)  # Llamada a la función
print('Resultado de la suma:', resultado)  # Imprimir el resultado de la función   


def resta(a, b):
    return a - b  # Definición de la función            
resultado_resta = resta(10, 5)  # Llamada a la función
print('Resultado de la resta:', resultado_resta)  # Imprimir el resultado de la
