import pytest

from src.calculadora import Calc, CalcError

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
