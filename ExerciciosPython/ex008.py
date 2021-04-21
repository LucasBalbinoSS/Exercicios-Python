n = float(input('\033[1;35mDigite uma quantia em metros para que a mesma seja convertida em centímetros e milímetros: \033[m'))

print('\033[34m%.3f metro(s) equivale a %.3f centímetros\n%.3f metro(s) Equivale a %.3f milímetros \033[m'
      % (n, n * 100, n, n * 1000))
