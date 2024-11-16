def calcular_notas_moedas(valor):

    cedulas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    quantidade = {}

    for cedula_moeda in cedulas_moedas:
        quantidade[cedula_moeda] = int(valor // cedula_moeda)
        valor -= quantidade[cedula_moeda] * cedula_moeda 

    valor_saque = float(input("Digite o valor do saque (em reais): ").replace(',', '.'))
    if valor_saque <= 0:
        print("O valor do saque deve ser positivo.")
    else:
        notas_moedas = calcular_notas_moedas(valor_saque)
        print("Quantidade de cédulas e moedas:")
        for valor, qtd in notas_moedas.items():
            if qtd > 0:
                print(f"R$ {valor:.2f}: {qtd}")
print("Entrada inválida! Por favor, insira um valor numérico decimal positivo, usando vírgula ou ponto para os centavos.")
