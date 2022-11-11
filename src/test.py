from src.verificador import Verificador

lista = [1, 2, 3, 4]

ver = Verificador()

ver.retirarNumero(lista)

for i in range(len(lista)):
    print("lista: " + lista[i])