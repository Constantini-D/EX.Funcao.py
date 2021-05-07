# valores de triangulo maiores que zero
# comprimento de um lado tem que ser menor que a soma dos dois lados

base = float(input(f'Digite o valor da base: '))
if base <= 0:
    print(f'valor de {base} inválido! digite novamente ')
    base = float(input(f'Digite o valor da base: '))


hipotenusa = float(input(f'Digite o valor da hipotenusa: '))
if hipotenusa <= 0:
    print(f'valor de {hipotenusa} inválido! digite novamente ')
    hipotenusa = float(input(f'Digite o valor da hipotenusa: '))


altura = float(input(f'Digite o valor da altura: '))
if altura <= 0:
    print(f'valor de {altura} inválido! digite novamente ')
    altura = float(input(f'Digite o valor da altura: '))


def triangulo(base, hipotenusa, altura):
    if base+hipotenusa > altura or base+altura > hipotenusa or hipotenusa+altura > base:
         if base==hipotenusa and base==altura:
            print(f'triangulo é equilátero')
         elif base==hipotenusa or base==altura or altura==hipotenusa:

             print('Triangulo isoceles  ')
         else:
               print("triangulo escaleno")


triangulo(base, hipotenusa, altura)






