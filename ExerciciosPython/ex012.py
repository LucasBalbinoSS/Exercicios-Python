p = float(input('Informe o preço do produto: R$'))

print('Seu produto de valor {:.2f}R$, com 5% de desconto vai para {:.2f}R$!'.format(p, p - (p * 5/100)))