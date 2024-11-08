class NumeroMasGrande:
    print("Este programa muestra el numero mas grande de 3 numeros")
    while True:
        num1 = int(input("Dame el numero 1: "))
        num2 = int(input("Dame el numero 2: "))
        num3 = int(input("Dame el numero 3: "))

        if num1 > num2 and num1 > num3:
            print(f"El numero {num1} es el mas grande")
        if num2 > num1 and num2 > num3:
            print(f"El numero {num2} es el mas grande")
        if num3 > num1 and num3 > num2:
            print(f"El numero {num2} es el mas grande")
        
        salida = input( "Quieres volver a valorar algun otro numero ? (si/no)")
        if salida != "si":
            break
