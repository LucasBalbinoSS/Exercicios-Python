print()
print('JOGO DA ADIVINHAÇÃO')
print()

from random import randint
na = randint(0, 5)
n = int(input('Tente adivinhar o número que o computador está pensando: '))

while n != na:
    n = int(input('Errou! o número não é %i\nTente acertar novamente: ' % n))

print()
print('UAU, parabéns!, você acertou!, o número é ', na)
