#função que lerá sexo, olhos,cabelo e idade
#fazer matriz para receber os dados


import random


# Ler os dados da tabela
def leitura(n):
    chaves = ['sexo', 'idade', 'olhos', 'cabelos']
    genero = 'Masculino', 'Feminino'
    olhos = 'Azul', 'Castanho'
    cabelos = 'Loiro', 'Preto', 'Castanho'
    """
    Os valores Random estavam sobrescrevendo sempre que a função era chamada
    dados = [[(random.choice(genero)),
              (random.randint(0, 100)),
              (random.choice(olhos)),
              (random.choice(cabelos)),
              ]
              """
    dados = [[input('sexo - (homem, mulher): ').title(), input('Idade: '),
              input('Cor dos olhos - A para azuis e C para castanhos: ').title(),
              input('Cor dos cabelos - L para louros, P para pretos e C - para castanhos: ').title()]
             for pessoa in range(0, n)]
    fichamento =[dict(zip(chaves, dados[i])) for i in range(0,n)]
    return fichamento


# MEDIA DE IDADE DAS PESSOAS Com olho castanho e cabelo preto
def media_idade(fichamento):
    soma = 0
    for i in range(len(fichamento)):
        if fichamento[i]['olhos'] == 'C':
            if fichamento[i]['cabelos'] == 'P':
                soma = soma+int(fichamento[i]['idade'])
    return soma


# devolver a maior idade entre os habitantes
def maior_idade(fichamento):
    maior = 0
    for i in range(len(fichamento)):
        print(fichamento[i])
        if int(fichamento[i]['idade']) > maior:
            maior = int(fichamento[i]['idade'])
    return maior



cadastros = leitura(2)
soma = media_idade(cadastros)
print(soma)
maior=maior_idade(cadastros)
print(f'a maior idade entre os membros é{maior}')