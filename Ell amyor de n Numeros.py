import random

def leer_tamano():
   
    while True:
        try:
            tamano = int(input("Ingresa el tamaño del arreglo: "))
            if tamano > 0:
                return tamano
            else:
                print("El tamaño debe ser un número positivo. Inténtalo nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def inicializar_arreglo(tamano):
    
    return [random.randint(1, 100) for _ in range(tamano)]

def encontrar_mayor(arreglo):
    
    return max(arreglo)

# Programa principal
def main():
    tamano = leer_tamano()
    arreglo = inicializar_arreglo(tamano)
    print(f"Arreglo generado: {arreglo}")
    mayor = encontrar_mayor(arreglo)
    print(f"El mayor valor del arreglo es: {mayor}")


