km = float(input('\033[1;31mQuantos Km rodados? '))
d = int(input('Quantos dias? '))
tp = (d * 60) + (km * 0.15)

print('\033[37mO total a pagar é de R$%.2f' % tp)
