s = float(input('\033[35mQual é o salário do funcionário?: R$ '))

print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber: {:.2f}R$'.format(s, s + (s * 15/100)))
