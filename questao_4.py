dias_por_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Entrada de dados
dia_inicial = int(input("Informe o dia inicial: "))
mes_inicial = int(input("Informe o mês inicial (1 a 12): "))
dia_final = int(input("Informe o dia final: "))
mes_final = int(input("Informe o mês final (1 a 12): "))

# Validação de entradas
if mes_inicial not in dias_por_mes:
    print("Erro: Mês inicial inválido. Deve estar entre 1 e 12.")
elif mes_final not in dias_por_mes:
    print("Erro: Mês final inválido. Deve estar entre 1 e 12.")
elif not (1 <= dia_inicial <= dias_por_mes[mes_inicial]):
    print(f"Erro: Dia inicial inválido para o mês {mes_inicial}. Deve estar entre 1 e {dias_por_mes[mes_inicial]}.")
elif not (1 <= dia_final <= dias_por_mes[mes_final]):
    print(f"Erro: Dia final inválido para o mês {mes_final}. Deve estar entre 1 e {dias_por_mes[mes_final]}.")
elif (mes_inicial > mes_final) or (mes_inicial == mes_final and dia_inicial > dia_final):
    print("Erro: A data inicial deve ser anterior ou igual à data final.")
else:
    # Cálculo dos dias decorridos
    if mes_inicial == mes_final:
        # Meses iguais: apenas a diferença entre os dias
        dias_passados = dia_final - dia_inicial
    else:
        # Meses diferentes: soma dias restantes no mês inicial + dias entre os meses + dias do mês final
        dias_restantes_primeiro_mes = dias_por_mes[mes_inicial] - dia_inicial
        dias_entre_meses = sum(dias_por_mes[m] for m (mes_inicial + 1, mes_final))
        dias_passados = dias_restantes_primeiro_mes + dias_entre_meses + dia_final

    print(f"Dias decorridos: {dias_passados}")


