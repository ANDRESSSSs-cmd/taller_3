def calcular_salario(horas_trabajadas, tarifa_por_hora):
    # Cálculo del salario base
    if horas_trabajadas > 40:
        horas_regulares = 40
        horas_extras = horas_trabajadas - 40
        salario_base = (horas_regulares * tarifa_por_hora) + (horas_extras * tarifa_por_hora * 1.5)
    else:
        salario_base = horas_trabajadas * tarifa_por_hora

    return salario_base


def calcular_bono_antiguedad(salario_base, antiguedad):
    # Cálculo del bono por antigüedad
    if antiguedad >= 5:
        return salario_base * 0.05
    else:
        return 0


def calcular_comision(ventas):
    # Cálculo de la comisión por ventas
    if ventas > 1000:
        return (ventas - 1000) * 0.02
    else:
        return 0


def calcular_descuento(salario_bruto):
    # Cálculo de los descuentos según el salario bruto
    if salario_bruto <= 1000:
        descuento = salario_bruto * 0.10
    elif salario_bruto <= 2000:
        descuento = (1000 * 0.10) + ((salario_bruto - 1000) * 0.05)
    else:
        descuento = (1000 * 0.10) + (1000 * 0.05) + ((salario_bruto - 2000) * 0.03)

    return descuento


def main():
    print("Bienvenido a la calculadora de salarios con bonificaciones.")

    # Solicitar datos al usuario
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
    antiguedad = int(input("Ingrese los años de antigüedad en la empresa: "))
    ventas = float(input("Ingrese el total de ventas realizadas (si aplica): "))

    # Calcular salario base
    salario_base = calcular_salario(horas_trabajadas, tarifa_por_hora)

    # Calcular bonificaciones
    bono_antiguedad = calcular_bono_antiguedad(salario_base, antiguedad)
    comision = calcular_comision(ventas)

    # Salario bruto antes de descuentos
    salario_bruto = salario_base + bono_antiguedad + comision

    # Calcular descuentos
    descuento = calcular_descuento(salario_bruto)

    # Calcular salario neto
    salario_neto = salario_bruto - descuento

    # Mostrar resumen
    print("\nResumen del salario:")
    print(f"Salario base: ${salario_base:.2f}")
    print(f"Bono por antigüedad: ${bono_antiguedad:.2f}")
    print(f"Comisión por ventas: ${comision:.2f}")
    print(f"Salario bruto: ${salario_bruto:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Salario neto final: ${salario_neto:.2f}")


if __name__ == "__main__":
    main()
