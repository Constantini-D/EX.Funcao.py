#função que lerá sexo, olhos,cabelo e idade
#fazer matriz para receber os dados


import random


def pessoa():
    individuo = [[] for c in range(0, 4)]

    print('[  Sexo    ][   Olhos   ][  Cabelo  ][  Idade  ]')
    for l in range(0, 4):
        for c in range(0, 4):
            soma = 0
            index = 0
            genero = 'Masculino', 'Feminino'
            olho = 'Azul', 'Castanho'
            cabelos = 'Loiro', 'Preto', 'Castranho'
            sexo = random.choice(genero)     #input('digite os valores de sexo:')
            individuo[l].append(sexo)
            olhos = random.choice(olho)      #input('digite os valores de olhos:')
            individuo[l].append(olhos)
            cabelo = random.choice(cabelos)  #input('digite os valores de cabelo: ')
            individuo[l].append(cabelo)
            idade = random.randint(0, 99)
            individuo[l].append(idade)
            if olhos == 'Castanho' and cabelo == 'Preto':
                soma = soma+idade
                index = index+1

            print(f'[{individuo[l][c]:^10}]', end='')
        print('')









pessoa()