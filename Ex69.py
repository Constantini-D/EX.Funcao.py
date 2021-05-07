print('simplificar função')


def deno_nume():
    nominador = int(input('Digite o valor do nominador: '))
    denominador = int(input('Digite o valor do denominador: '))
    return nominador, denominador


def reduzir_funcao(nominador, denominador):
    for simplificador in range(1, 1000):
        if nominador%simplificador==0:
            if denominador%simplificador==0:
                divisor=simplificador
    a = nominador/divisor
    b = denominador/divisor
    print(f' a função {nominador}/{denominador} ficará {a}/{b}')
    return a, b


def operacoes(nominador, denominador):
    soma=nominador+denominador
    subtracao = nominador - denominador
    divisao = nominador / denominador
    multiplicacao=nominador * denominador
    return print(f'soma: {soma},subtracao: {subtracao},divisao: {round(divisao,2)}, multiplicao: {multiplicacao}')


nomi, deno = deno_nume()
#reduzir_funcao(nomi, deno)
operacaoNomi, operacaoDeno = reduzir_funcao(nomi, deno)
operacoes(operacaoNomi, operacaoDeno)