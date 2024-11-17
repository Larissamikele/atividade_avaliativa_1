def calcular_tarifa(minutos):
    
    horas = minutos / 60
    valor_total = 0.0
    
    if horas <= 2:

        valor_total = horas * 8
    elif horas <= 4:
        
        valor_total = (2 * 8) + ((horas - 2) * 5)
    elif horas <= 12:
        
        valor_total = (2 * 8) + (2 * 5) + ((horas - 4) * 3)
    else:
        
        valor_total = 30
    
    return round(valor_total, 2)


minutos = int(input("Digite o número de minutos que o veículo permaneceu no estacionamento: "))


valor = calcular_tarifa(minutos)

print(f'O valor a ser pago é R$ {valor}')
