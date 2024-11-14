hora_partida = int(input('informe o minuto parado (0 a 59): '))
litro_combustivel = float(input('informe os litros de combustivel'))
preco_combustivel = float(input('digite o valor do litro'))
distancia = float(input('informe a distancia pecorrida (em km): '))
partida_minuto = hora_partida * 60 + minuto_partida
chegada_minuto = hora_chegada * 60 + minuto_chegada
tempo_total_minutos = chegda_minuto - partida_minuto
tempo_parado_minuto = segundo_parado / 60 
tempo_viajem_minutos = tempo_total_minutos - tempo_parado_minuto
consumo_medio = distancia / litros_combustivel
custo_total = litros_conbustivel * preco_combustivel

print('/n--- detalhes_viajem ---')
print(f'tempo total de viajem (incluindo paradas): {tempo_total_minutos}')
print(f'tempo de viajem em movimento: {tempo_viajem_minutos:.2f} minutos')