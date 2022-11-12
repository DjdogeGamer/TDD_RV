from src.verificador import Verificador

ver = Verificador()

lista1 = [2, 3, 5]
lista2 = [4, 5, 2]
lista3 = [7, 8, 18]

ver.retirarNumero(lista1)
print(lista1)
ver.retirarNumero(lista2)
print(lista2)
ver.retirarNumero(lista3)
print(lista3)

n1 = 2
n2 = 3
n3 = 6

print(ver.verificaPrimo(n1))
print(ver.verificaPrimo(n2))
print(ver.verificaPrimo(n3))
