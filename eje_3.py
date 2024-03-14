def calcular_frecuencia(mensaje):
    frecuencias = {}
    mensaje = mensaje.lower()
    for caracter in mensaje:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    frecuencias = dict(sorted(frecuencias.items(), key=lambda x: x[1], reverse=True))
    return frecuencias

def construir_tabla(frecuencias):
    tabla = {}
    simbolos_ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    codigo =""
    for simbolo, frecuencia in simbolos_ordenados:
        tabla[simbolo] = codigo
        codigo = '0' + codigo
    return tabla

def codificar_mensaje(mensaje, tabla):
    mensaje_codificado = ""
    for caracter in mensaje:
        mensaje_codificado += tabla[caracter]
    return mensaje_codificado

def mostrar_tabla(tabla):
    print("Simbolo\t|\tCodigo")
    print("---------------------------")
    for simbolo, codigo in tabla.items():
        print(f"{simbolo}\t|\t{codigo}")

def dividir_tabla(frecuencias):
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    parte_1 = {}
    parte_2 = {}
    suma_total = sum(frecuencias.values())
    mitad = suma_total // 2 if suma_total % 2 == 0 else suma_total // 2 +1
    suma_p1 = 0


    for simbolo, frecuencia in frecuencias_ordenadas:
        diferencia_p1 = abs(suma_p1 - mitad)
        diferencia_p2 = abs(suma_total - suma_p1 - mitad)
        if suma_p1 < suma_total - suma_p1:
            parte_1[simbolo] = frecuencia
            suma_p1 += frecuencia
        else:
            parte_2[simbolo] = frecuencia
    
    return parte_1, parte_2, suma_p1, suma_total - suma_p1

def main():
    mensaje = input("Ingrese el mensaje que desee: ")
    frecuencias = calcular_frecuencia(mensaje)

    print("\nTabla de frecuencias:")
    mostrar_tabla(frecuencias)

    parte_1, parte_2, suma_p1, suma_p2 = dividir_tabla(frecuencias)

    print("\nParte 1 de la tabla:")
    mostrar_tabla(parte_1)
    print("Suma de frecuencias en la parte 1:", suma_p1)

    print("\nParte 2 de la tabla:")
    mostrar_tabla(parte_2)
    print("Suma de frecuencias en la parte 2:", suma_p2)


if __name__ == "__main__":
    main()