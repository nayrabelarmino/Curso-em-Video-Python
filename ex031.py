km = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(km))
curta = km * 0.50
longa = km * 0.45
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}.'.format(curta))
else:
    print('E o preço da sua passagem será de R${:.2f}.'.format(longa))
