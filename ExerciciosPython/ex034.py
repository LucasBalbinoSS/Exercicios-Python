s = float(input('Qual é o seu salário atual? R$'))

if s > 1250:
    print('O seu salário, com 10% de aumento, de {:.3f}, se torna {:.3f}'.format(s, s + (s * 10 / 100)))
elif s <= 1250:
    print('O seu salário, com 15% de aumento, de {:.3f}, se torna {:.3f}'.format(s, s + (s * 15 / 100)))
