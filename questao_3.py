
hora_partida = int(input('Informe a hora de partida (0 a 23): '))
minuto_partida = int(input('Informe o minuto de partida (0 a 59): '))
hora_chegada = int(input('Informe a hora de chegada (0 a 23): '))
minuto_chegada = int(input('Informe o minuto de chegada (0 a 59): '))
segundo_parado = int(input('Informe o tempo parado (em segundos): '))
litros_combustivel = float(input('Informe os litros de combustível consumidos: '))
preco_combustivel = float(input('Digite o valor do litro do combustível: '))
distancia = float(input('Informe a distância percorrida (em km): '))


if not (0 <= hora_partida <= 23 and 0 <= minuto_partida <= 59):
    print("Horário de partida inválido.")
    exit()
if not (0 <= hora_chegada <= 23 and 0 <= minuto_chegada <= 59):
    print("Horário de chegada inválido.")
    exit()
if segundo_parado < 0 or litros_combustivel <= 0 or preco_combustivel <= 0 or distancia <= 0:
    print("Valores inválidos fornecidos.")
    exit()


partida_minuto = hora_partida * 60 + minuto_partida
chegada_minuto = hora_chegada * 60 + minuto_chegada
tempo_total_minutos = chegada_minuto - partida_minuto
tempo_parado_minuto = segundo_parado / 60
tempo_viajem_minutos = tempo_total_minutos - tempo_parado_minuto


if tempo_total_minutos <= 0:
    print("O horário de chegada deve ser maior que o horário de partida.")
    exit()


consumo_medio = distancia / litros_combustivel
custo_total = litros_combustivel * preco_combustivel


print('\n--- Detalhes da Viagem ---')
print(f'Tempo total de viagem (incluindo paradas): {tempo_total_minutos} minutos')
print(f'Tempo de viagem em movimento: {tempo_viajem_minutos:.2f} minutos')
print(f'Consumo médio: {consumo_medio:.2f} km/l')
print(f'Custo total de combustível: R$ {custo_total:.2f}')
