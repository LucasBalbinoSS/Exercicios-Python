nome = str(input('\033[35mInforme seu nome completo: ')).strip().title()
print()
print(nome)

if 'Silva' in nome:
    print('Sim!, seu nome contém "Silva"!')
else:
    print('Não!, seu nome não contém "Silva"')
