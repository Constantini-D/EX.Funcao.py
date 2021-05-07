#imprimir vetor normal
#imprimir inverso
#somar valor dos vetores


import random


def funcao():

    tamanho = int(input(f'Digite o tamanho do vetor: '))
    vetor = []
    soma = 0

    for laco in range(tamanho):
        a = laco*random.randint(0, 10)
        soma = soma + a
        vetor.append(a)
    print(vetor)
    ordem = sorted(vetor)
    print(ordem[::-1])
    return print(soma)

funcao()