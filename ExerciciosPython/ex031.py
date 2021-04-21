print()
print('\033[35mR$0.50 por Km para viagens de até 200Km\nR$0.45 por Km para viagens acima de 200Km')
print()

km = float(input('\033[32mQual é a distância da viagem em Km: '))
print('Sua viagem será de %.1fKm' % km)

if km <= 200:
    print('\033[31mO custo da sua viagem é: R$%.2f' % (km * 0.50))
else:
    print('\033[35mO custo da sua viagem é: R$%.2f' % (km * 0.45))

# também é possível fazer dessa forma:
# km = float(input('Qual é a distância da viagem em Km:'))
# print('Sua viagem será de %.1fKm' % km)
# p = km * 0.50 if km <= 200 else km * 0.45
# print('O custo da sua viagem será de R$%.2f' % p)
