print()
print('\033[32mJOGO DA ADIVINHAÇÃO')
print()

from random import randint
na = randint(0, 5)
n = int(input('\033[35mTente adivinhar o número que o computador está pensando: '))

while n != na:
    n = int(input('\033[32mErrou! o número não é %i\nTente acertar novamente: ' % n))

print()
print('\033[35mUAU, parabéns!, você acertou!, o número é ', na)
