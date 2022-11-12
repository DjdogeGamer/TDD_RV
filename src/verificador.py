
class Verificador:
    maior = 0
    menor = 0

    def verificaPrimo(self, num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            else:
                return True

    """
    retirar o maior e o menor valor de uma lista de números naturais, EXCETO se algum deles for primo.
    No caso de algum deles ou ambos serem primo deve ser retirado o próximo número maior ou menor.
    Caso a lista esteja vazia, deve retornar uma lista vazia.
    Caso o tamanho da lista seja um ou dois e composta por números não primos, deve retornar uma lista vazia.
    Se houver algum número primo, deve retornar a lista somente com os números primos.
    Para os demais casos, deve retornar uma lista sem o maior e o menor valor.
    """

    def retirarNumero(self, lista):
        if len(lista) == 0:
            return []
        elif len(lista) == 1:
            if self.verificaPrimo(lista[0]):
                return lista
            else:
                return []
        elif len(lista) == 2:
            if self.verificaPrimo(lista[0]) and self.verificaPrimo(lista[1]):
                return lista
            elif self.verificaPrimo(lista[0]):
                return [lista[0]]
            elif self.verificaPrimo(lista[1]):
                return [lista[1]]
            else:
                return []
        else:
            self.maior = max(lista)
            self.menor = min(lista)
            if self.verificaPrimo(self.maior) and self.verificaPrimo(self.menor):
                lista.remove(self.maior)
                lista.remove(self.menor)
                return lista
            elif self.verificaPrimo(self.maior):
                lista.remove(self.maior)
                return lista
            elif self.verificaPrimo(self.menor):
                lista.remove(self.menor)
                return lista
            else:
                lista.remove(self.maior)
                lista.remove(self.menor)
                return lista