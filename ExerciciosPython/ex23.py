# print()
#
# print('NÚMEROS & MATEMÁTICA')
#
# print()
#
# n = str(input('Digite um número de 0 á 9999: '))
#
# print('Unidades:', n[3], '\nDezenas:', n[2], '\nCentenas:', n[1], '\nMilhar:', n[0])

n = int(input('\033[35mDigite um número de zero a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número %i...' % n, '\nUnidades: %i' % u, '\nDezenas: %i' % d,
      '\nCentenas: %i' % c, '\nMilhar: %i' % m)