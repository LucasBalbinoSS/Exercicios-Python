a = int(input('\033[35mInforme um ano qualquer para saber se essse ano é bissexto ou não (coloque 0 para saber sobre o ano atual): '))

from datetime import date
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    if a == 0:
        a = date.today().year
    if a <= 2020:
        print('\033[37mSim, o ano %i foi um ano bissexto' % a)
    else:
        print('\033[35mSim, o ano %i será um ano bissexto' % a)
elif a <= 2019:
    print('Não... o ano %i não foi um ano bissexto' % a)
elif a > 2021:
    print('Não... o ano %i não será um ano bissexto' % a)
print()
print('Obrigado pela preferência')
