import shutil
from datetime import datetime

def renomeia_arquivo():
    dia_atual = datetime.today().day
    mes_atual = datetime.today().month
    ano_atual = datetime.today().year

    nome_arquivo = ("relatorio_excel" + "_" + f"{str(ano_atual)}" + f"{str(mes_atual)}" + f"{str(dia_atual)}" + ".xlsx")

    return nome_arquivo

origem_arquivo = (r"C:\Users\lixow\OneDrive\Documentos\Projeto - Financeiro\Main\templates\relatorio_excel.xlsx")
destino_arquivo = (f"C:\\Users\\lixow\\OneDrive\\Documentos\\Projeto - Financeiro\\Main\\templates\\OLD\\{renomeia_arquivo()}" )
shutil.copy(origem_arquivo, destino_arquivo)