#pegar dois numeros
#retornar qual é o maior

a=int(input(f'digite o primeiro valor: '))
b=int(input(f'digite o primeiro valor: '))

def maior(a, b):
    if a>b:
        return print(f'o valor {a} é maior que {b}')
    return print(f'o valor {b} é maior que {a}')
maior(a,b)