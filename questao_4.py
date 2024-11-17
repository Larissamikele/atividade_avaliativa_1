
dias_por_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

dia_inicial = int(input("Informe o dia inicial: "))
mes_inicial = int(input("Informe o mês inicial: "))
dia_final = int(input("Informe o dia final: "))
mes_final = int(input("Informe o mês final: "))


if mes_inicial not in dias_por_mes or mes_final not in dias_por_mes:
    print("Erro: Mês válido de (1 a 12).")
elif not (1 <= dia_inicial <= dias_por_mes[mes_inicial]):
    print(f"Erro: Dia inicial inválido para o mês {mes_inicial}.")
elif not (1 <= dia_final <= dias_por_mes[mes_final]):
    print(f"Erro: Dia final inválido para o mês {mes_final}.")
elif (mes_inicial > mes_final) or (mes_inicial == mes_final and dia_inicial > dia_final):
    print("Erro: A data inicial deve ser anterior à data final.")
else:
    if mes_inicial == mes_final:
        dias_passados = dia_final - dia_inicial
    else:
        dias_restantes_primeiro_mes = dias_por_mes[mes_inicial] - dia_inicial
        dias_entre_meses = sum(dias_por_mes[m] for m in range(mes_inicial + 1, mes_final))
        dias_passados = dias_restantes_primeiro_mes + dias_entre_meses + dia_final

    print(f"Dias decorridos: {dias_passados}")

