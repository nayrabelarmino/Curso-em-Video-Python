salário = float(input('Qual é o salário do funcionário? R$'))
if salário <=1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava \033[33mR${:.2f}\033[m, agora passa a ganhar \033[32mR${:.2f}\033[m.'.format(salário, novo))
