largura = float(input('Largura de sua parede: '))
alt = float(input('Altura de sua parede: '))
a = largura * alt

print('Sua parede tem a dimensão de %.2f x %.2f e sua área é de %.3fm²' % (largura, alt, a))

tinta = a / 2

print('Para pintar sua parede, você precisará de %.3fl de tinta!' % tinta)
