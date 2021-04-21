vel = float(input('\033[35mInforme a velocidade do carro (a cada Km/h acima do limite, você pagará R$7,00): '))
multa = 0

if vel > 80:
    print()
    print('Você acabou de ser multado, e deve pagar a quantia de %.2f ', (vel - 80) * (multa + 7.00))
else:
    print()
    print('Bom dia!\nDirija com segurança!, não passe de 80Km')
