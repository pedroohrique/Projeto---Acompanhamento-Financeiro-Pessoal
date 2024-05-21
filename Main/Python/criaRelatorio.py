from dataImport import *
from openpyxl import load_workbook, writer

class Gera_relatorio():
    def __init__(self) -> None:
        pass

    
    def configura_arquivo(self):

        caminho_arquivo_xlsx = (r"C:\Users\lixow\OneDrive\Documentos\Projeto - Financeiro\Main\templates\relatorio_excel.xlsx")
        arquivo_excel = load_workbook(filename=caminho_arquivo_xlsx)
        aba_planilha_selecionada = arquivo_excel['Visão Geral']
        dados_relatorio = ImportData()
        
        aba_planilha_selecionada['B3'] = dados_relatorio.obtem_valor_total_gasto()
        aba_planilha_selecionada['F3'] = dados_relatorio.obtem_gasto_cartao()
        aba_planilha_selecionada['J3'] = dados_relatorio.obtem_demais_valores()
        aba_planilha_selecionada['B8'] = 3750
        aba_planilha_selecionada['B13'] = 17779
        aba_planilha_selecionada['G19'] = dados_relatorio.gasto_por_categoria()[100]
        aba_planilha_selecionada['G20'] = dados_relatorio.gasto_por_categoria()[200]
        aba_planilha_selecionada['G21'] = dados_relatorio.gasto_por_categoria()[300]
        aba_planilha_selecionada['G22'] = dados_relatorio.gasto_por_categoria()[400]
        aba_planilha_selecionada['G23'] = dados_relatorio.gasto_por_categoria()[500]
        aba_planilha_selecionada['G24'] = dados_relatorio.gasto_por_categoria()[600]
        aba_planilha_selecionada['G25'] = dados_relatorio.gasto_por_categoria()[700]
        aba_planilha_selecionada['G26'] = dados_relatorio.gasto_por_categoria()[800]
        aba_planilha_selecionada['G27'] = dados_relatorio.gasto_por_categoria()[900]
        aba_planilha_selecionada['G28'] = dados_relatorio.gasto_por_categoria()[1000]
        aba_planilha_selecionada['G29'] = dados_relatorio.gasto_por_categoria()[1100]
        arquivo_excel.save(filename=caminho_arquivo_xlsx)