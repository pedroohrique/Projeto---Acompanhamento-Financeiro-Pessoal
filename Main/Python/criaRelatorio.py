from dataImport import *
from openpyxl import load_workbook, writer
from datetime import datetime
import calendar

class Gera_relatorio():
    def __init__(self) -> None:
        pass

    def obtem_diasRestantes(self):
        dia_atual = datetime.today().day
        mes_atual = datetime.today().month
        ano_atual = datetime.today().year
        qtd_dias = calendar.monthrange(ano_atual, mes_atual)    
        dias_restantes = (qtd_dias[1] - dia_atual)
        return dias_restantes
    
    def configura_arquivo(self):

        caminho_arquivo_xlsx = (r"C:\Users\Pedro Henrique\Documents\Projeto - Financeiro\Main\templates\relatorio_excel.xlsx")
        arquivo_excel = load_workbook(filename=caminho_arquivo_xlsx)
        aba_planilha_selecionada = arquivo_excel['Visão Geral']
        dados_relatorio = ImportData()
        
        aba_planilha_selecionada['B3'] = dados_relatorio.obtem_valor_total_gasto()
        aba_planilha_selecionada['F3'] = dados_relatorio.obtem_gasto_cartao()
        aba_planilha_selecionada['J3'] = dados_relatorio.obtem_demais_valores()
        aba_planilha_selecionada['B8'] = 3750
        aba_planilha_selecionada['B12'] = "Gasto diário disponível:"
        aba_planilha_selecionada['G12'] = (aba_planilha_selecionada['B8'].value - aba_planilha_selecionada['B3'].value) / self.obtem_diasRestantes()
        aba_planilha_selecionada['B15'] = dados_relatorio.obtem_aplicacao_financ()
        aba_planilha_selecionada['G21'] = dados_relatorio.gasto_por_categoria()[100]
        aba_planilha_selecionada['G22'] = dados_relatorio.gasto_por_categoria()[200]
        aba_planilha_selecionada['G23'] = dados_relatorio.gasto_por_categoria()[300]
        aba_planilha_selecionada['G24'] = dados_relatorio.gasto_por_categoria()[400]
        aba_planilha_selecionada['G25'] = dados_relatorio.gasto_por_categoria()[500]
        aba_planilha_selecionada['G26'] = dados_relatorio.gasto_por_categoria()[600]
        aba_planilha_selecionada['G27'] = dados_relatorio.gasto_por_categoria()[700]
        aba_planilha_selecionada['G28'] = dados_relatorio.gasto_por_categoria()[800]
        aba_planilha_selecionada['G29'] = dados_relatorio.gasto_por_categoria()[900]
        aba_planilha_selecionada['G30'] = dados_relatorio.gasto_por_categoria()[1000]
        aba_planilha_selecionada['G31'] = dados_relatorio.gasto_por_categoria()[1100]
        arquivo_excel.save(filename=caminho_arquivo_xlsx)