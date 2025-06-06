# Trifecta
#

import math

while True:
    entrada = input("Ingresa un número entero (0 para salir): ")

    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        numero = int(entrada)
        if numero == 0:
            print("El programa ha finalizado.")
            break
        print("El programa ha iniciado.")

        
        frase = input("Ingresa una palabra o frase: ")
        cantidad_caracteres = len(frase)
        print(f"La cantidad de caracteres es: {cantidad_caracteres}")

        
        if cantidad_caracteres >= 0:
            factorial = math.factorial(cantidad_caracteres)
            print(f"El factorial de {cantidad_caracteres} es: {factorial}")

            if factorial % 2 == 0:
                print("El resultado es un número *par*.")
            else:
                print("El resultado es un número *impar*.")
    else:
        print("Entrada inválida. El programa ha finalizado.")
        break       