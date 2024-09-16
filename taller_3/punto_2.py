def solicitar_numero_unico(mensaje, numeros_existentes):
    while True:
        try:
            numero = int(input(mensaje))
            if numero in numeros_existentes:
                print("El número ya ha sido ingresado. Por favor, ingrese un número diferente.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def main():
    print("Bienvenido al comparador y analizador de números.")

    numeros = []

    # Solicitar tres números únicos
    while len(numeros) < 3:
        numero = solicitar_numero_unico("Ingrese un número entero diferente: ", numeros)
        numeros.append(numero)

    # Análisis
    mayor = max(numeros)
    menor = min(numeros)
    suma = sum(numeros)
    promedio = suma / 3

    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    cantidad_pares = len(pares)
    cantidad_impares = len(impares)

    # Mostrar resumen
    print("\nResumen del análisis:")
    print(f"Números ingresados: {numeros}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")
    print(f"Suma de los números: {suma}")
    print(f"Promedio de los números: {promedio:.2f}")

    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")

    if cantidad_pares > cantidad_impares:
        print("Hay más números pares que impares.")
    elif cantidad_impares > cantidad_pares:
        print("Hay más números impares que pares.")
    else:
        print("La cantidad de números pares e impares es igual.")


if __name__ == "__main__":
    main()