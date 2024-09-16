def main():
    print("Bienvenido al sistema de compras.")

    total_articulos = 0
    total_sin_descuento = 0.0

    # Ingreso de artículos
    while True:
        articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() == 'fin':
            break

        try:
            precio = float(input(f"Ingrese el precio del artículo '{articulo}': "))
            cantidad = int(input(f"Ingrese la cantidad de '{articulo}': "))

            if cantidad <= 0 or precio < 0:
                print("La cantidad debe ser un número positivo y el precio no puede ser negativo.")
                continue

            total_articulos += cantidad
            total_sin_descuento += precio * cantidad

        except ValueError:
            print("Entrada inválida. Por favor, ingrese valores numéricos válidos.")

    # Calcular descuento
    if total_articulos >= 5:
        descuento = 0.20
    elif total_articulos >= 3:
        descuento = 0.10
    else:
        descuento = 0.0

    total_con_descuento = total_sin_descuento * (1 - descuento)

    # Determinar método de pago y posibles cargos adicionales
    if total_articulos >= 3:
        metodo_pago = "Tarjeta"
        total_final = total_con_descuento * 1.02
    else:
        metodo_pago = "Efectivo"
        total_final = total_con_descuento

    # Mostrar resumen
    print("\nResumen de la compra:")
    print(f"Número total de artículos: {total_articulos}")
    print(f"Total antes del descuento: ${total_sin_descuento:.2f}")
    print(f"Descuento aplicado: {descuento * 100:.0f}%")
    print(f"Total después del descuento: ${total_con_descuento:.2f}")
    print(f"Método de pago recomendado: {metodo_pago}")
    print(f"Total final {'con cargo de tarjeta' if metodo_pago == 'Tarjeta' else ''}: ${total_final:.2f}")


if __name__ == "__main__":
    main()

