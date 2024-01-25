import json
import csv
from datetime import datetime, timedelta

registros = []
rendimentos = {}
#FUNÇÃO CRIAR REGISTRO#
def criar_registro(data, tipo, valor):
    if tipo not in ['receita', 'despesa', 'investimento', '1', '2', '3']:
        print("Tipo inválido, os tipos válidos são: receita, despesa e investimento ou digite o número da opção.")
        return 

    if tipo == 'receita' or tipo == '1':
        tipo = 'receita'
        valor = valor

    if tipo == 'despesa' or tipo == '2':
        tipo = 'despesa'
        valor = -valor

  
    registro = {
        'tipo' : tipo,
        'valor' : valor,
        'data' : data,
        'dia' : data.day,
        'mes' : data.month,
        'ano' : data.year,
    }

    if tipo == 'investimento' or tipo == '3':
        tipo = 'investimento'
        registro['montante'] = valor
        rendimentos[len(registros)] = 0

    registros.append(registro)

#FUNÇÃO LER REGISTRO#

def ler_registros(filtro=None, campo=None):
    if filtro is None or campo is None:
        return registros
    
    return [registro for registro in registros if filtro in registro.values()]

#FUNÇÕES DE CONSULTA DO REGISTRO#
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

#FUNÇÃO DELETAR#
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
    investimentos_atualizados = 0

    for indice, registro in enumerate(registros):
        if registro['tipo'] == 'investimento':
            montante = registro['montante']
            taxa_diaria = 0.418
            dias_passados = (datetime.now() - registro['data']).days
            rendimento = montante * (1 + taxa_diaria) ** dias_passados
            registros[indice]['rendimento'] = rendimento - montante

            investimentos_atualizados += 1

    if investimentos_atualizados > 0:
        print(f"Atualizou {investimentos_atualizados} investimentos.")
    else:
        print("Não há registros de investimentos a atualizar.")

    return investimentos_atualizados

#EXPORTAÇÃO#
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
