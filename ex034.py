#Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <=1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava \033[33mR${:.2f}\033[m, agora passa a ganhar \033[32mR${:.2f}\033[m.'.format(salário, novo))
