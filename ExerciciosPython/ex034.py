s = float(input('\033[35mQual é o seu salário atual? R$'))

if s > 1250:
    print('\033[34mO seu salário, com 10% de aumento, de {:.3f}, se torna {:.3f}'.format(s, s + (s * 10 / 100)))
elif s <= 1250:
    print('\033[35mO seu salário, com 15% de aumento, de {:.3f}, se torna {:.3f}'.format(s, s + (s * 15 / 100)))
