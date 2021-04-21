nome = input('\033[35mInforme seu nome para ver suas variações: ')

print('Em maiúsculas:', nome.upper())

print()

print('Em minúsculas:', nome.lower())

print()

nome = nome.split()
junto = ''.join(nome[0:])

print('O seu nome, ao todo, contém %s letras' % len(junto))

print()

print('\033[35mSeu primeiro nome contém %s letras' % len(nome[0]))
