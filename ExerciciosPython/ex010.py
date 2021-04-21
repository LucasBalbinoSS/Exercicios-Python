r = float(input('\033[33mQuanto dinheiro você tem na carteira?  R$'))
print('Com R$%.2f você pode comprar U$%.1f\033[m' % (r, r / 3.27))
