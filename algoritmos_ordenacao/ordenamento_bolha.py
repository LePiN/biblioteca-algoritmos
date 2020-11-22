entrada_teste = [66, 38, 39, 57, 70, 35, 21, 75, 83, 11, 41, 20, 68, 30, 24, 59]

def ordenar_numeros_pelo_metodo_bolha(conjunto_numerico: list) -> list:
    for contador_externo in range(len(conjunto_numerico) - 1):
        for contador_interno in range(len(conjunto_numerico) - 1):
            primeiro_verificado, segundo_verificado = (
                conjunto_numerico[contador_interno], conjunto_numerico[contador_interno + 1])
            if conjunto_numerico[contador_interno] > conjunto_numerico[contador_interno + 1]:
                conjunto_numerico[contador_interno] = segundo_verificado
                conjunto_numerico[contador_interno + 1] = primeiro_verificado
    return conjunto_numerico

print(ordenar_numeros_pelo_metodo_bolha(entrada_teste))