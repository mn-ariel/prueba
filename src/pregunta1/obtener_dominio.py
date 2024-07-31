def obtener_dominio(correo):
    try:
        partes = correo.split('@')
        if len(partes) != 2 or partes[1] == '':
            raise ValueError("La variable ingresada no tiene el formato correcto, por lo tanto no se puede extraer el dominio")
        return partes[1]
    except Exception as e:
        raise ValueError("La variable ingresada no tiene el formato correcto, por lo tanto no se puede extraer el dominio")
