import math
co = float(input('\033[34mComprimento do cateto oposto: '))
ca = float(input('\033[35mComprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print('\033[mA hipotenusa vai medir %.2f' % hi)
