entrada_teste = [66, 38, 39, 57, 70, 35, 21, 75, 83, 57, 41, 20, 68, 30, 24, 59]


def ordenar_numeros_crescente_pelo_metodo_bolha(conjunto_numerico: list) -> list:
    """
    Funcao que organiza uma lista de numeros de modo crescente atraves do algoritmo apelidado de bolha.

    Args:
        conjunto_numerico (list): obrigatoriamente uma lista composta exclusivamente de valores numericos.

    Returns:
        list: uma lista com valores numericos organizados em uma sequencia crescente.
    
    Observations:
        Aceita valores repetidos, e consegue lidar com numeros inteiros e reais simultaneamente.
    """
    for passagem in range(len(conjunto_numerico) - 1):
        for posicao in range(len(conjunto_numerico) - 1):
            if conjunto_numerico[posicao] > conjunto_numerico[posicao + 1]:
                conjunto_numerico[posicao], conjunto_numerico[posicao + 1] = (
                    conjunto_numerico[posicao + 1], conjunto_numerico[posicao])
    return conjunto_numerico



def ordenar_numeros_decrescente_pelo_metodo_bolha(conjunto_numerico: list) -> list:
    """
    Funcao que organiza uma lista de numeros de modo decrescente atraves do algoritmo apelidado de bolha.

    Args:
        conjunto_numerico (list): obrigatoriamente uma lista composta exclusivamente de valores numericos.

    Returns:
        list: uma lista com valores numericos organizados em uma sequencia decrescente.
    
    Observations:
        Aceita valores repetidos, e consegue lidar com numeros inteiros e reais simultaneamente.
    """
    for passagem in range(len(conjunto_numerico) - 1):
        for posicao in range(len(conjunto_numerico) - 1):
            if conjunto_numerico[posicao] < conjunto_numerico[posicao + 1]:
                conjunto_numerico[posicao], conjunto_numerico[posicao + 1] = (
                    conjunto_numerico[posicao + 1], conjunto_numerico[posicao])
    return conjunto_numerico


def ordenar_numeros_pelo_metodo_bolha(conjunto_numerico: list, tipo_ordenamento=True) -> list:
    """
    Funcao que organiza uma lista de numeros de modo crescente ou decrescente atraves do 
    algoritmo apelidado de bolha.

    Args:
        conjunto_numerico (list): obrigatoriamente uma lista composta exclusivamente de valores numericos.
        tipo_ordenamento(boolean): Caso verdadeiro ou nao informado, ordena de forma crescente caso contrario 
        ordena de maneira descrescente.

    Returns:
        list: uma lista com valores numericos organizados em uma sequencia crescente ou decrescente.
    
    Observations:
        Aceita valores repetidos, e consegue lidar com numeros inteiros e reais simultaneamente.
    """
    if tipo_ordenamento:
        tipo_comparacao = lambda posicao_1, posicao_2: posicao_1 > posicao_2
    else: 
        tipo_comparacao = lambda posicao_1, posicao_2: posicao_1 < posicao_2
    
    for passagem in range(len(conjunto_numerico) - 1):
        for posicao in range(len(conjunto_numerico) - 1):
            if tipo_comparacao(conjunto_numerico[posicao], conjunto_numerico[posicao + 1]):
                conjunto_numerico[posicao], conjunto_numerico[posicao + 1] = (
                    conjunto_numerico[posicao + 1], conjunto_numerico[posicao])
    return conjunto_numerico

class ConjuntoOrdenadoBolha():
    
    def __init__(self, conjunto_numerico: list, tipo_ordenamento=True):
        self.conjunto_numerico = conjunto_numerico
        self.tipo_ordenamento = tipo_ordenamento
        self._conjunto_ordenado = self._ordenar_conjunto()


    def _ordenar_conjunto(self, tipo_ordenamento=True):
        self._conjunto_ordenado = self.conjunto_numerico.copy()
        self.tipo_ordenamento = tipo_ordenamento
        
        if self.tipo_ordenamento:
            tipo_comparacao = lambda posicao_1, posicao_2: posicao_1 > posicao_2
        else: 
            tipo_comparacao = lambda posicao_1, posicao_2: posicao_1 < posicao_2
        
        for passagem in range(len(self._conjunto_ordenado) - 1):
            for posicao in range(len(self._conjunto_ordenado) - 1):
                if tipo_comparacao(self._conjunto_ordenado[posicao], self._conjunto_ordenado[posicao + 1]):
                    self._conjunto_ordenado[posicao], self._conjunto_ordenado[posicao + 1] = (
                        self._conjunto_ordenado[posicao + 1], self._conjunto_ordenado[posicao])
        return self._conjunto_ordenado
    
    def __str__(self) -> str:
        return (
            f"Conjunto original: {self.conjunto_numerico}\n"
            f"Tipo de ordenamento: {'crescente' if self.tipo_ordenamento else 'decrescente'}\n"
            f"Conjunto ordenado: {self._conjunto_ordenado}"
        )


#Verifincando a funcao que organiza de forma crescente.
print(ordenar_numeros_crescente_pelo_metodo_bolha(entrada_teste), '\n')
#Verificando a funcao que organiza de forma decrescente.
print(ordenar_numeros_decrescente_pelo_metodo_bolha(entrada_teste), '\n')
#Verificando a funcao que organiza da forma desejada. Caso crescente.
print(ordenar_numeros_pelo_metodo_bolha(entrada_teste), '\n')
#Verificando a funcao que organiza da forma desejada. Caso decrescente.
print(ordenar_numeros_pelo_metodo_bolha(entrada_teste, tipo_ordenamento=False), '\n')
#Verificando a classe que organiza de forma customizada. Caso crescente.
print(ConjuntoOrdenadoBolha(entrada_teste), '\n')
#Verificando a classe que organiza de forma customizada. Caso decrescente.
print(ConjuntoOrdenadoBolha(entrada_teste, tipo_ordenamento=False), '\n')
