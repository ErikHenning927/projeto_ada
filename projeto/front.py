import main
from datetime import datetime

def solicitar_registro():
    tipo = input("Informe o tipo (receita, despesa ou investimento): ")
    valor = float(input("Informe o valor: "))
    data_str = input("Informe a data no formato YYYY-MM-DD: ")
    data = datetime.strptime(data_str, '%Y-%m-%d')
    
    main.criar_registro(data, tipo, valor)

def main_menu():
    while True:
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
        print("0. Sair")

        escolha = input("Escolha a opção desejada (0-9): ")

        if escolha == '1':
            solicitar_registro()
        elif escolha == '2':
            print(main.ler_registros())
        elif escolha == '3':
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
            indice = int(input("Informe o índice do registro a ser deletado: "))
            main.deletar_registro(indice)
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
