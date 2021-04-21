n1 = float(input('\033[1;35mDigite a primeira nota: \033[m'))
n2 = float(input('\033[36mDigite a segunda nota: \033[m'))
m = (n1 + n2) / 2

print('\033[1;32mA média entre %.1f e %.1f é %.1f\033[m' % (n1, n2, m))
