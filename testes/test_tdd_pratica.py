import pytest

#from src.calculadora import Calc, CalcError
from src.verificador import Verificador

# Funcionalidades Principais
# 1 - Retirar o maior e o menor valor de uma lista de números naturais EXCETO se algum deles for primo.
# 2 - Caso a lista esteja vazia, deve retornar uma lista vazia.
# 3 - Caso o tamanho da lista seja um ou dois e composta por números não primos, deve retornar uma lista vazia.
#     Se houver algum número primo, deve retornar a lista somente com os números primos.
# 4 - Para os demais casos, deve retornar uma lista sem o maior e o menor valor .
# Numeros Primos: 2, 3, 5, 7, 11, 13, 17

# Teste para retirar o maior e o menor valor de uma lista de números naturais EXCETO se algum deles for primo.

@pytest.mark.parametrize("lista, res_esp", [( [2, 3, 5], [3] ), ( [4, 5, 2], [4])])
def test_retirarNumero(lista, res_esp):
    verificador = Verificador()
    res = verificador.retirarNumero(lista)
    assert res_esp == res

@pytest.mark.parametrize("num, res_esp", [(2, True), (3, True), (6, False), (7, True), (11, True), (13, True), (17, True)])
def test_verificaPrimo(num, res_esp):
    verificador = Verificador()
    res = verificador.verificaPrimo(num)
    assert res_esp == res

