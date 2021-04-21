nome = input('Informe seu nome para ver suas variações: ')

print('Em maiúsculas:', nome.upper())

print()

print('Em minúsculas:', nome.lower())

print()

nome = nome.split()
junto = ''.join(nome[0:])

print('O seu nome, ao todo, contém %s letras' % len(junto))

print()

print('Seu primeiro nome contém %s letras' % len(nome[0]))
