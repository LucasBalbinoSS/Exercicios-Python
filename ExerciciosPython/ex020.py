import random

nomes = input('\033[35mDigite quatro nomes para sortea-los em uma sequência: ')
sorteio = nomes.split()

nm1 = (sorteio[0])
nm2 = (sorteio[1])
nm3 = (sorteio[2])
nm4 = (sorteio[3])

random.shuffle(sorteio)

print('A sequência de apresentação dos trabalhos é: ', sorteio)
