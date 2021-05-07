#matriz para somar os elementos a cima da diagonal principal


import random


def somar_matriz():

    tamanho = int(input(f'Digite o tamanho da matriz: '))
    matriz=[[] for c in range(0, tamanho)]
    soma=0
    for l in range(0, tamanho):
        for c in range(0, tamanho):
            #a=int(input('digite:'))
            a = 1 * random.randint(0, 30)
            matriz[l].append(a)
            print(f'[{matriz[l][c]:^5}]', end='')
            if (c) > (l):
                soma = soma+a
        print('')
    """for c in range(0, tamanho):
        for l in range(0, tamanho):
            print(f'[{matriz[l][c]:^5}]', end='')
        print('')"""
    return print(soma)





somar_matriz()