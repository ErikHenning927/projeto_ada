from faker import Faker
import random
from datetime import datetime
import main

fake = Faker()

def gerar_registros_aleatorios(n):
    for _ in range(n):
        tipo = random.choice(['receita', 'despesa', 'investimento'])
        valor = round(random.uniform(100, 10000), 2)  

        data = fake.date_between(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31))
        data = datetime.strptime(str(data), '%Y-%m-%d')

        if tipo == 'despesa':
            valor = -valor 

        main.criar_registro(data, tipo, valor)

gerar_registros_aleatorios(10)
