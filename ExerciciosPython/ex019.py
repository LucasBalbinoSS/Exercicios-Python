import random

nomes = input('\033[35mEscreva o nome de quatro alunos: ')
dados = nomes.split()

n1 = (dados[0])
n2 = (dados[1])
n3 = (dados[2])
n4 = (dados[3])

print(dados, sep=',')
print('O escolhido foi:', random.choice(dados), '!')
