def identificar_nivel_ventas(venta, categoria):
    incremento = 50
    if categoria == 1 or categoria == 0:
        incremento = incremento * categoria
    else:
        raise ValueError("La variable categoria solo puede contener valores de 0 y 1")

    if venta <= 60 + incremento:
        return "Baja"
    elif 61 + incremento <= venta <= 80 + incremento:
        return "Media"
    else:
        return "Alta"
