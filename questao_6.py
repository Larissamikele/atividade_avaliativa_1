from datetime import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    idade = hoje.year - nascimento.year
    if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
        idade -= 1
    return idade

def calcular_tempo_contr(data_contribuicao):
    hoje = datetime.today()
    inicio_contribuicao = datetime.strptime(data_contribuicao, "%d/%m/%Y")
    tempo_contribuicao = hoje.year - inicio_contribuicao.year
    if hoje.month < inicio_contribuicao.month or (hoje.month == inicio_contribuicao.month and hoje.day < inicio_contribuicao.day):
        tempo_contribuicao -= 1
    return tempo_contribuicao

sexo = input('Informe o sexo do usuário (feminino/masculino): ')
if sexo != "masculino" and sexo != "feminino":
    sexo = input('Opção inválida! Informe "masculino" ou "feminino": ')

data_nas = input('Informe a data de nascimento (DD/MM/AAAA): ')
data_contr = input('Informe a data de contribuição (DD/MM/AAAA): ')

print('\nInformações adquiridas:')
print(f'Sexo: {sexo}')
print(f'Data de nascimento: {data_nas}')
print(f'Data de início de contribuição: {data_contr}')


idade = calcular_idade(data_nas)
tempo_contribuicao = calcular_tempo_contr(data_contr)


if sexo == "masculino":
    aposentadoria_idade = 65
    aposentadoria_tempo = 35
else:
    aposentadoria_idade = 62
    aposentadoria_tempo = 30

if idade >= aposentadoria_idade and tempo_contribuicao >= 15:
    aposentadoria_idade_data = datetime.strptime(data_nas, "%d/%m/%Y").replace(year=datetime.today().year + aposentadoria_idade - idade)
else:
    aposentadoria_idade_data = "Não pode se aposentar por idade"


if tempo_contribuicao >= aposentadoria_tempo:
    aposentadoria_tempo_data = datetime.strptime(data_contr, "%d/%m/%Y").replace(year=datetime.today().year + aposentadoria_tempo - tempo_contribuicao)
else:
    aposentadoria_tempo_data = "Não pode se aposentar por tempo de contribuição"

print('\nInformações sobre a aposentadoria:')
print(f'Idade: {idade} anos')
print(f'Tempo de contribuição: {tempo_contribuicao} anos')


if isinstance(aposentadoria_idade_data, datetime):
    print(f"Aposentadoria por Idade: {aposentadoria_idade_data.strftime('%d/%m/%Y')}")
else:
    print(f"Aposentadoria por Idade: {aposentadoria_idade_data}")


if isinstance(aposentadoria_tempo_data, datetime):
    print(f"Aposentadoria por Tempo de Contribuição: {aposentadoria_tempo_data.strftime('%d/%m/%Y')}")
else:
    print(f"Aposentadoria por Tempo de Contribuição: {aposentadoria_tempo_data}")
