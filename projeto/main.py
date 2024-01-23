import json
import csv
from datetime import datetime, timedelta

registros = []
rendimentos = {}

def criar_registro(data, tipo, valor):
    if tipo not in ['receita', 'despesa', 'investimento']:
        print("Tipo inválido, os tipos válidos são: receita, despesa e investimento.")
        return 

    if tipo == "despesa":
        valor = -valor

    registro = {
        'tipo' : tipo,
        'valor' : valor,
        'data' : data,
        'dia' : data.day,
        'mes' : data.month,
        'ano' : data.year,
    }

    if tipo == 'investimento':
        registro['montante'] = valor
        rendimentos[len(registros)] = 0

    registros.append(registro)

def ler_registros(filtro=None, campo=None):
    if filtro is None or campo is None:
        return registros
    
    return [registro for registro in registros if filtro in registro.values()]

def consultar_por_data(data):
    return [registro for registro in registros if registro['data'] == data]

def consultar_por_tipo(tipo):
    return [registro for registro in registros if registro['tipo'] == tipo]

def consultar_por_valor(valor):
    return [registro for registro in registros if registro['valor'] == valor]

def organizar_por(chave):
    grupos = {}
    for registro in registros:
        valor = registro[chave]
        if valor not in grupos:
            grupos[valor] = 0
        grupos[valor] += registro['valor']

    return grupos

def deletar_registro(indice):
    if indice < 0 or indice >= len(registros):
        print("Indice inválido.")
        return
    if registros[indice]['tipo'] == 'investimento':
        del rendimentos[indice]
    del registros[indice]

def atualizar_registro(indice, tipo=None, valor=None, data=None):
    if indice < 0 or indice >= len(registros):
        print ("Índice inválido.")
        return
    
    registro = registros[indice]

    if tipo is not None:
        registro['tipo'] = tipo
    if valor is not None:
        registro['valor'] = valor
    if data is not None:
        registro['data'] = data
    
    if registro['tipo'] == 'investimento':
        rendimentos[indice] = 0


def atualizar_rendimentos():
    for indice, registro in enumerate(registros):
        if registro['tipo'] == 'investimento':
            montante = registro['montante']
            taxa_diaria = 0.418
            dias_passados = (datetime.now() - registro['data']).days
            rendimento = montante * (1 + taxa_diaria) ** dias_passados
            rendimento[indice] = rendimento - montante

def exportar_relatorio(formato='json'):
    if formato not in ['json', 'csv']:
        print("Formato de exportação inválido. Formatos válidos: json e csv")
        return
    
    relatorio = {'registros': registros, 'rendimentos': rendimentos}

    if formato == 'json':
        def converter_datetime(obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d')
            raise TypeError("Não é serializado")
        
        with open('relatorio.json', 'a') as file:
            file.write('\n')
            json.dump(relatorio, file, indent=2, default=converter_datetime)

    elif formato == 'csv':
        with open('relatorio.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=relatorio.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(relatorio)

data_registro = datetime(2024, 1, 10)
criar_registro(data_registro, 'receita', 3500)

print(ler_registros())

atualizar_rendimentos()

data_registro = datetime(2024, 1, 15)

print ("\norganizar por tipo 1")
print (organizar_por('tipo'))

atualizar_registro(0, valor=7000)
atualizar_registro(0, data=data_registro)
atualizar_registro(0, tipo='investimento')

print("\nExportando relatório em CSV:")
exportar_relatorio('csv')

print("\nExportando relatório em JSON:")
exportar_relatorio('json')

data_consulta = datetime(2024, 1, 15)
tipo_consulta = 'investimento'
valor_consulta = 7000

print ("\norganizar por tipo 2")
print (organizar_por('tipo'))


print(ler_registros())

print ("\nConsulta por data:")
resultados_por_data = consultar_por_data(data_consulta)
print (resultados_por_data)

print ("\nConsulta por tipo:")
resultados_por_tipo = consultar_por_tipo(tipo_consulta)
print (resultados_por_tipo)

print ("\nConsulta por valor:")
resultados_por_valor = consultar_por_valor(valor_consulta)
print (resultados_por_valor)

deletar_registro(0)

print(ler_registros())
