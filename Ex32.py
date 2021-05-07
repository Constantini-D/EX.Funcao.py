
# simplificar função
# armazenar o valor de resto zero até um valor mil
print('simplificar função')
nominador = int(input('Digite o valor do nominador: '))
denominador = int(input('Digite o valor do denominador: '))


def reduzir_funcao(nominador, denominador):
    for simplificador in range(1, 1000):
        if nominador%simplificador==0:
            if denominador%simplificador==0:
                divisor=simplificador
    return print(f' a função {nominador}/{denominador} ficará {nominador/divisor}/{denominador/divisor}')


reduzir_funcao(nominador, denominador)