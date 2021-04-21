print('\033[1m-=' * 20)
print('\033[1;32mAnalisador de Triângulos\033[m')
print('\033[1m-=\033[m' * 20)

c1 = float(input('Informe o comprimento da primeira reta: '))
c2 = float(input('Informe o comprimento da segunda reta: '))
c3 = float(input('Informe o comprimento da terceira reta: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print()
    print('\033[1;32mSim\033[m, é possível formar um triângulo!')
else:
    print()
    print('\033[1;31mNão\033[m é possível formar um triângulo...')
