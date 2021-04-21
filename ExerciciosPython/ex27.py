nome = str(input('\033[35mDigite seu nome completo: ')).strip()
print(nome)

nome2 = nome.split()
print(len(nome2))
print('Seu primeiro nome é %s' % nome2[0])

print('Seu último nome é %s' % nome2[len(nome2)-1])
