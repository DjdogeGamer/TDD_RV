import pytest

#from src.calculadora import Calc, CalcError
from src.verificador import Verificador

"""
# teste para somar 3 e 4, resultado tem que ser 7
def test_soma34():
    calculadora = Calc()

    res_calc = calculadora.soma(3,4)
    assert res_calc == 7

# teste para somar 4 e 5, resultado tem que ser 9
def test_soma45():
    calculadora = Calc()
    res_calc = calculadora.soma(4,5)
    assert res_calc == 9

@pytest.mark.parametrize("a,b,res_esp",[(3,4,7),(4,5,9),(1000,1,1001)])
def test_soma(a,b,res_esp):
    calculadora = Calc()
    res = calculadora.soma(a,b)
    assert res_esp == res

@pytest.mark.parametrize("a,b,res_esp",[(3,"4",7),(4,"5",9),("1000",1,1001)])
def test_soma_string(a,b,res_esp):
    calculadora = Calc()
    with pytest.raises(CalcError):
        res_esp = calculadora.soma(a,b)
"""

# Funcionalidades Principais
# 1 - Retirar o maior e o menor valor de uma lista de números naturais EXCETO se algum deles for primo.
# 2 - Caso a lista esteja vazia, deve retornar uma lista vazia.
# 3 - Caso o tamanho da lista seja um ou dois e composta por números não primos, deve retornar uma lista vazia.
#     Se houver algum número primo, deve retornar a lista somente com os números primos.
# 4 - Para os demais casos, deve retornar uma lista sem o maior e o menor valor .
# Numeros Primos: 2, 3, 5, 7, 11, 13, 17

# Teste para retirar o maior e o menor valor de uma lista de números naturais EXCETO se algum deles for primo.

@pytest.mark.parametrize("lista, res_esp", [([7, 8, 18], [8, 18])])
def test_retirarNumero(lista, res_esp):
    verificador = Verificador()
    res = verificador.retirarNumero(lista)
    assert res_esp == res

@pytest.mark.parametrize("num, res_esp", [(2, True), (3, True), (6, False), (7, True), (11, True), (13, True), (17, True)])
def test_verificaPrimo(num, res_esp):
    verificador = Verificador()
    res = verificador.verificaPrimo(num)
    assert res_esp == res

