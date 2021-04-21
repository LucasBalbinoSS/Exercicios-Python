n = str(input('\033[35mDigite três números (separe-os com vírgula): ')).strip()
ns = n.split(', ')

n1 = int(ns[0])
n2 = int(ns[1])
n3 = int(ns[2])

print()
print('Você digitou os números: %i, %i e %i' % (n1, n2, n3))
print('Dos números que você digitou, o maior deles é o %i' % max(n1, n2, n3))
print('Dos números que você digitou, o menor deles é o %i' % min(n1, n2, n3))
