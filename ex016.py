#Crie um programa que leira um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

'''import math
num = float(input('Digite um valor: '))
inteiro = math.floor(num)
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, inteiro))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, int(num)))
