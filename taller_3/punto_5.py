def calcular_descuento_base(marca):
    # Descuentos por marca
    descuentos = {
        "Honda": 0.05,
        "Yamaha": 0.08,
        "Suzuki": 0.10
    }
    return descuentos.get(marca, 0.02)  # 2% para otras marcas


def calcular_descuento_adicional(dia, feriado):
    # Descuentos adicionales basados en el día
    descuentos_dia = {
        "Martes": 0.12,
        "Sábado": 0.18
    }

    if feriado:
        return 0.25
    else:
        return descuentos_dia.get(dia, 0)  # 0% si no es martes ni sábado


def calcular_descuento_total(precio_base, descuento_base, descuento_adicional):
    # Calcula el descuento total aplicable
    descuento_total = descuento_base + descuento_adicional

    # Asegura que el descuento total no supere el 30%
    if descuento_total > 0.30:
        descuento_total = 0.30

    return descuento_total


def main():
    print("Bienvenido al sistema de ventas de motocicletas.")

    # Solicitar información al usuario
    while True:
        try:
            precio_base = float(input("Ingrese el precio base de la motocicleta: $"))
            if precio_base <= 0:
                print("El precio base debe ser un número positivo. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número decimal válido.")

    marca = input("Ingrese la marca de la motocicleta (Honda, Yamaha, Suzuki, u Otra): ").capitalize()
    dia = input("Ingrese el día de la semana de la compra: ").capitalize()
    feriado = input("¿Es el día de la compra feriado? (Sí/No): ").strip().lower() == "sí"

    # Calcular descuentos
    descuento_base = calcular_descuento_base(marca)
    descuento_adicional = calcular_descuento_adicional(dia, feriado)
    descuento_total = calcular_descuento_total(precio_base, descuento_base, descuento_adicional)

    # Calcular el precio final
    ahorro_total = precio_base * descuento_total
    precio_final = precio_base - ahorro_total

    # Mostrar resumen
    print("\nResumen de la compra:")
    print(f"Precio base de la motocicleta: ${precio_base:.2f}")
    print(f"Descuento por marca ({marca}): {descuento_base * 100:.2f}%")
    print(f"Descuento adicional ({dia} {'y feriado' if feriado else ''}): {descuento_adicional * 100:.2f}%")
    print(f"Descuento total aplicado: {descuento_total * 100:.2f}%")
    print(f"Ahorro total para el cliente: ${ahorro_total:.2f}")
    print(f"Precio final de la motocicleta: ${precio_final:.2f}")


if __name__ == "__main__":
    main()
