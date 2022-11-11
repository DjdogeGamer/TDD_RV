import numbers

class VerificadorError(Exception):
    pass

class Verificador:
    maior = 0
    menor = 0

    def verificaPrimo(self, num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return True
                    break
            else:
                return False

    def retirarNumero(self, lista):
        # retirar o maior e o menor valor de uma lista de números naturais, EXCETO se algum deles for primo.

        maior = max(lista)
        menor = min(lista)

        # Verifica Maior
        while(lista.verificaPrimo(maior) == False):
            maior = max(lista)
            lista.pop(maior)

        # Verifica Menor
        while(lista.verificaPrimo(menor) == False):
            menor = min(lista)
            lista.pop(menor)

        return lista

    """
    def soma(self,op1,op2):
        self._check_type(op1)
        self._check_type(op2)
        return op1+op2

    def _check_type(self, op):
        if not isinstance(op,numbers.Number):
            raise VerificadorError()
    """