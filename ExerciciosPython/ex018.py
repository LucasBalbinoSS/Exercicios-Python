import math
an = float(input('\033[35mInforme um ângulo qualquer: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('O SENO do ângulo %.2f é igual a %.2f\nCOSSENO igual a %.2f\nTANGENTE igual a %.2f' % (an, sen, cos, tan))
