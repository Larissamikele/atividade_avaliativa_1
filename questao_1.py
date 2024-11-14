numero = int(input('Informe um número de até quatro algarismos: '))

# Verifica se o número está dentro do intervalo desejado
if numero > 9999 or numero < 0:
    print('Erro: Informe um número de até 4 algarismos entre 0 e 9999!')
else:
    l = numero // 1000  # Algarismo dos milhares
    numero = numero % 1000
    c = numero // 100    # Algarismo das centenas
    numero = numero % 100
    d = numero // 10     # Algarismo das dezenas
    u = numero % 10      # Algarismo das unidades

    soma = l + c + d + u
    print(f'A soma dos algarismos é {soma}')