num = int(input('Me diga um número qualquer: '))
result = num % 2
if result == 0:
    print('O número \033[32m{}\033[m é \033[36mPAR\033[m.'.format(num))
else:
    print('O número \033[32m{}\033[m é \033[36mÍMPAR\033[m.'.format(num))
