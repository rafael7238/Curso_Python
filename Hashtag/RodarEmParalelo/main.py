import time
import os
import pandas as pd
from joblib import Parallel, delayed
import numpy
import openpyxl

tempo_inicial = time.time()

arquivos = os.listdir()


def calcular_faturamento(arquivo):
    if "xlsx" in arquivo:
        tabela = pd.read_excel(arquivo)
        faturamento = tabela["Valor Final"].sum()
        return f"Faturamento da Loja {arquivo.replace('.xlsx','')} foi de R${faturamento:,.2f}"

# N_JOBS é depende do número de Cors do computador. O -1 fala que executa com o maior capacidade
resultado = Parallel(n_jobs=10)(delayed(calcular_faturamento)
                               (arquivo) for arquivo in arquivos)
print(resultado)
print(f"Demorou: {time.time() - tempo_inicial}")