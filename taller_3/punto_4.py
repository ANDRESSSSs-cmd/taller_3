import numpy as np


def solicitar_calificaciones():
    calificaciones = []
    for i in range(1, 6):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación {i} (entre 0 y 10): "))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número decimal válido.")
    return calificaciones


def calcular_estadisticas(calificaciones):
    promedio = np.mean(calificaciones)
    mediana = np.median(calificaciones)
    desviacion_estandar = np.std(calificaciones)
    max_calificacion = np.max(calificaciones)
    min_calificacion = np.min(calificaciones)

    return promedio, mediana, desviacion_estandar, max_calificacion, min_calificacion


def determinar_estado(promedio):
    if promedio >= 9:
        return "Excelente"
    elif promedio >= 7:
        return "Bueno"
    elif promedio >= 5:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_recomendacion(estado, desviacion_estandar):
    if estado == "Excelente":
        return "¡Felicidades! Mantén tu excelente desempeño y sigue así."
    elif estado == "Bueno":
        if desviacion_estandar < 1:
            return "Bien hecho. Tu consistencia en las calificaciones es notable. ¡Sigue trabajando para alcanzar la excelencia!"
        else:
            return "Buena labor. Trabaja en mejorar la consistencia de tus calificaciones para lograr un desempeño aún mejor."
    elif estado == "Aprobado":
        if desviacion_estandar < 1:
            return "Has aprobado, pero te recomendamos trabajar en mejorar tus calificaciones y mantener una mayor consistencia."
        else:
            return "Necesitas mejorar. Enfócate en mejorar tus calificaciones y mantener una mayor consistencia."
    else:  # Reprobado
        if desviacion_estandar < 1:
            return "Es necesario que te esfuerces más. La baja consistencia en tus calificaciones indica que necesitas mejorar tus estudios."
        else:
            return "Es urgente que tomes medidas para mejorar tus calificaciones. Trabaja en una estrategia de estudio más efectiva."


def main():
    print("Bienvenido al sistema de análisis de calificaciones.")

    # Solicitar calificaciones al usuario
    calificaciones = solicitar_calificaciones()

    # Calcular estadísticas
    promedio, mediana, desviacion_estandar, max_calificacion, min_calificacion = calcular_estadisticas(calificaciones)

    # Determinar el estado del estudiante
    estado = determinar_estado(promedio)

    # Generar recomendación
    recomendacion = generar_recomendacion(estado, desviacion_estandar)

    # Mostrar resumen
    print("\nResumen del análisis:")
    print(f"Calificaciones ingresadas: {calificaciones}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")
    print(f"Calificación más alta: {max_calificacion:.2f}")
    print(f"Calificación más baja: {min_calificacion:.2f}")
    print(f"Estado del estudiante: {estado}")
    print(f"Recomendación: {recomendacion}")


if __name__ == "__main__":
    main()
