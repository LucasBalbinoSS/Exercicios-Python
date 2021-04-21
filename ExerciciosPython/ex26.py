name = str(input('Digite uma frase: ').strip()).upper()
ns = ''.join(name[0:])

print(ns)

print('Existem %s letra(s) "A" na frase' % ns.count('A'))

print()

print('A primeira aparição da letra "A" ocorreu na posição de número %s' % (ns.find('A')+1))

print('A última letra "A" aparece na posição de número %s' % ns.rfind('A'))
