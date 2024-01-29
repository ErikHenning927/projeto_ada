import main
from datetime import datetime
import os
import gerar

gerar.gerar_registros_aleatorios(10)



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def solicitar_registro():
    limpar_tela()

    tipos_validos = ['receita', 'despesa', 'investimento']

    tipo = input("Informe o tipo (receita, despesa ou investimento): ").lower()
    if tipo not in tipos_validos:
        print("Tipo inválido. Tipos válidos são: {}".format(', '.join(tipos_validos)))
        return

    try:
        valor = float(input("Informe o valor: "))
    except ValueError:
        print("Valor inválido. Certifique-se de fornecer um número.")
        return

    data_str = input("Informe a data no formato YYYY-MM-DD: ")
    try:
        data = datetime.strptime(data_str, '%Y-%m-%d')
    except ValueError:
        print("Formato de data inválido. Certifique-se de seguir o formato YYYY-MM-DD.")
        return
    
    main.criar_registro(data, tipo, valor)
def atualizar_registro():
    try:
        registro_id = int(input('Informe o registro: '))
        tipo = input('Informe um novo tipo: ')
        valor = float(input('Informe um novo valor: '))
        data_str = input('Informe uma nova data: ')
        if data_str:
            data = datetime.strptime(data_str, '%Y-%m-%d')
        else:
            data = None
        main.atualizar_registro(registro_id, tipo, valor, data)
        print('Registro  atualizado com sucesso! ')
    
    except ValueError:
        print('Erro ao atualizar registro! ')   
def main_menu():
    while True:
        
        print('=' * 30)
        print('{:^30}'.format('BEM VINDO - SANTA FINANCEIRA'))
        print('=' * 30)
        print("\n----- Menu Principal -----")
        print("1. Adicionar novo registro")
        print("2. Ler registros")
        print("3. Atualizar rendimentos")
        print("4. Exportar relatório em CSV")
        print("5. Exportar relatório em JSON")
        print("6. Consultar por data")
        print("7. Consultar por tipo")
        print("8. Consultar por valor")
        print("9. Deletar registro")
        print("10. Agrupar registro por mês")
        print("11. Atualizar registro")
        print("0. Sair")

        escolha = input("Escolha a opção desejada (0-9): ")
        limpar_tela()
        if escolha == '1':
            solicitar_registro()    
        elif escolha == '2':
            print(main.ler_registros())
        elif escolha == '3':
            print('Rendimentos atualizados! ')
            main.atualizar_rendimentos()
        elif escolha == '4':
            main.exportar_relatorio('csv')
        elif escolha == '5':
            main.exportar_relatorio('json')
        elif escolha == '6':
            data_consulta = input("Informe a data no formato YYYY-MM-DD: ")
            resultados_por_data = main.consultar_por_data(datetime.strptime(data_consulta, '%Y-%m-%d'))
            print(resultados_por_data)
        elif escolha == '7':
            tipo_consulta = input("Informe o tipo a ser consultado: ")
            resultados_por_tipo = main.consultar_por_tipo(tipo_consulta)
            print(resultados_por_tipo)
        elif escolha == '8':
            valor_consulta = float(input("Informe o valor a ser consultado: "))
            resultados_por_valor = main.consultar_por_valor(valor_consulta)
            print(resultados_por_valor)
        elif escolha == '9':
            registro_id = int(input("Informe o ID do registro a ser deletado: "))
            main.deletar_registro(registro_id)
        elif escolha == '10':
            total_mes = main.agrupar_por_mes()
            for mes_chave, total in total_mes.items():
                ano, mes = mes_chave
                print(f'Total para {mes}/{ano}: {total}')
        elif escolha == '11':
            atualizar_registro()  
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
