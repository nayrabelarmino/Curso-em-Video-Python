salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${}, com um aumento de 15%, passa a receber R${}'.format(salário, novo))
