import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import date, datetime
from database import database_connection
from criaRelatorio import Gera_relatorio

class RegistroDeGastos:
    def __init__(self, root):
        self.root = root
        self.janelaCadastro()
        
    def janelaCadastro(self):
        """Inicializa a janela de cadastro e seus componentes."""
        self.root.title("Registro de Gastos")    
        
        # Labels and Entries
        self.label_data = tk.Label(self.root, text="Data do Gasto:")
        self.entry_data = tk.Entry(self.root)
        self.label_valor = tk.Label(self.root, text="Valor do Gasto:")
        self.entry_valor = tk.Entry(self.root)
        self.label_descricao = tk.Label(self.root, text="Descrição:")
        self.entry_descricao = tk.Entry(self.root)
        self.label_local = tk.Label(self.root, text="Local:")
        self.entry_local = tk.Entry(self.root)
        self.label_forma = tk.Label(self.root, text="Forma Pagamento:")
        self.opcoes_forma = ['Cartão de Crédito', 'Cartão de Débito', 'Dinheiro', 'PIX', 'Saldo da Conta']
        self.combobox_forma = ttk.Combobox(self.root, values=self.opcoes_forma)
        self.label_parcelamento = tk.Label(self.root, text='Compra parcelada:')
        self.variavel_opcao = tk.StringVar()
        self.opcao1 = tk.Radiobutton(self.root, text="SIM", variable=self.variavel_opcao, value="SIM")
        self.opcao2 = tk.Radiobutton(self.root, text="NÃO", variable=self.variavel_opcao, value="NÃO")
        self.label_qtd_parcelas = tk.Label(self.root, text='Quantidade Parcelas:')
        self.spinbox_qtd_parcelas = tk.Spinbox(self.root, from_=0, to=15)
        self.label_categoria = tk.Label(self.root, text='Categoria:')
        self.opcoes_categoria = ['Alimentação', 'Moradia', 'Transporte', 'Saúde', 'Lazer e Entretenimento', 'Compras', 'Gastos Ocasionais', 'Investimentos e Aplicações', 'Pagamento Fatura', 'Educação', 'Outros']
        self.combobox_categoria = ttk.Combobox(self.root, values=self.opcoes_categoria)

        # Grid layout
        self.label_data.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
        self.entry_data.grid(row=0, column=1, padx=10, pady=5)
        self.label_valor.grid(row=1, column=0, padx=10, pady=5, sticky="w") 
        self.entry_valor.grid(row=1, column=1, padx=10, pady=5)
        self.label_descricao.grid(row=2, column=0, padx=10, pady=5, sticky="w")  
        self.entry_descricao.grid(row=2, column=1, padx=10, pady=5)
        self.label_local.grid(row=3, column=0, padx=10, pady=5, sticky="w")  
        self.entry_local.grid(row=3, column=1, padx=10, pady=5)
        self.label_forma.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.combobox_forma.grid(row=4, column=1, padx=10, pady=5)
        self.label_parcelamento.grid(row=5, column=0, padx=10, pady= 5, sticky="w")
        self.opcao1.grid(row=5,column=1, padx=10, pady= 5, sticky="w")
        self.opcao2.grid(row=5, column=1, padx=10, pady=5, sticky="e")  
        self.label_qtd_parcelas.grid(row=6, column=0, padx=10, pady=5, sticky="w")      
        self.spinbox_qtd_parcelas.grid(row=6, column=1, padx=10, pady=5) 
        self.label_categoria.grid(row=7, column=0, padx=10, pady=5, sticky="w")   
        self.combobox_categoria.grid(row=7, column=1, padx=10, pady=5)

    def obtem_dt_registro(self) -> date:
        """Obtém a data de registro atual."""
        return date.today()

    def obtem_dt_gasto(self) -> str:
        """Obtém e valida a data do gasto."""
        dt_gasto = self.entry_data.get()
        try:
            data_convertida = datetime.strptime(dt_gasto, '%d-%m-%Y').date()
            dt_registro = self.obtem_dt_registro()
            if data_convertida <= dt_registro:
                return data_convertida.strftime('%d-%m-%Y')
            else:
                messagebox.showinfo("Erro", "A data do gasto deve ser anterior ou igual à data de registro.")
                return None 
        except ValueError:
            messagebox.showinfo("Erro", "Informe uma data válida no formato dd-mm-yyyy.")
            return None  

    def obtem_valor_gasto(self) -> float:
        """Obtém e valida o valor do gasto."""
        valor_convertido = self.entry_valor.get()
        padrão = re.compile(r'^\d+(\.\d{1,2})?$')
        if re.match(padrão, valor_convertido):
            return float(valor_convertido)
        else:
            messagebox.showerror("Erro", "Informe um valor monetário válido!")
            return None

    def obtem_descricao(self) -> str:
        """Obtém e valida a descrição do gasto."""
        descricao = self.entry_descricao.get()
        if isinstance(descricao, str) and descricao.strip() and len(descricao) >= 5:
            return descricao
        else:
            messagebox.showerror("Erro", "Informe uma descrição válida!")
            return None

    def obtem_local(self) -> str:
        """Obtém e valida o local do gasto."""
        local = self.entry_local.get()
        if isinstance(local, str) and local.strip() and len(local) >= 5:
            return local
        else:
            messagebox.showerror("Erro", "Informe um local válido!")
            return None

    def obtem_forma_pagamento(self) -> int:
        """Obtém a forma de pagamento selecionada."""
        forma = self.combobox_forma.get().strip().upper()
        forma_pagamento_map = {
            'CARTÃO DE CRÉDITO': 100,
            'CARTÃO DE DÉBITO': 200,
            'DINHEIRO': 300,
            'PIX': 400,
            'SALDO DA CONTA': 500
        }
        return forma_pagamento_map.get(forma)

    def verifica_parcelamento(self) -> str:
        """Verifica se a compra é parcelada."""
        return 'S' if self.variavel_opcao.get().upper() == 'SIM' else 'N'

    def obtem_qtd_parcelas(self) -> int:
        """Obtém e valida a quantidade de parcelas."""
        try:
            qtd_parcelas = int(self.spinbox_qtd_parcelas.get())
            forma_pagamento = self.obtem_forma_pagamento()
            parcelamento = self.verifica_parcelamento()

            if qtd_parcelas < 0:
                raise ValueError("Informe uma quantidade válida!")
            elif qtd_parcelas > 0 and (forma_pagamento != 100 or parcelamento == 'N'):
                raise ValueError("Verifique as informações de parcelamento inseridas!")
            elif qtd_parcelas == 0 and (forma_pagamento == 100 or parcelamento == 'S'):
                raise ValueError("Verifique as informações de parcelamento inseridas!")
            return qtd_parcelas
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return None

    def obtem_categoria(self) -> int:
        """Obtém a categoria selecionada."""
        categoria = self.combobox_categoria.get().upper()
        categoria_map = {
            'ALIMENTAÇÃO': 100,
            'MORADIA': 200,
            'TRANSPORTE': 300,
            'SAÚDE': 400,
            'LAZER E ENTRETERIMENTO': 500,
            'COMPRAS': 600,
            'GASTOS OCASIONAIS': 700,
            'INVESTIMENTOS E APLICAÇÕES': 800,
            'PAGAMENTO FATURA': 900,
            'EDUCAÇÃO': 1000,
            'OUTROS': 1100
        }
        return categoria_map.get(categoria, None)

    def limpa_informacoes(self):
        """Limpa todas as entradas do formulário."""
        self.entry_data.delete(0, 'end')
        self.entry_descricao.delete(0, 'end')
        self.entry_local.delete(0, 'end')
        self.entry_valor.delete(0, 'end')
        self.combobox_forma.set('')
        self.combobox_categoria.set('')
        self.spinbox_qtd_parcelas.delete(0, 'end')

    def verifica_requisicao(self) -> bool:
        """Verifica se todas as informações necessárias foram inseridas corretamente."""
        try:
            return all([
                self.obtem_categoria(),
                self.obtem_qtd_parcelas() is not None,
                self.obtem_forma_pagamento() is not None,
                self.verifica_parcelamento(),
                self.obtem_descricao(),
                self.obtem_valor_gasto() is not None,
                self.obtem_dt_gasto(),
                self.obtem_local()
            ])
        except (ValueError, TypeError):
            return False

    def insere_info(self):
        """Insere as informações no banco de dados."""
        connection, cursor = database_connection()
        if connection and cursor and self.verifica_requisicao():
            cursor.execute(
                'INSERT INTO TB_REG_FINANC (DATA_REGISTRO, DATA_GASTO, VALOR, DESCRICAO, LOCAL_GASTO, PARCELAMENTO, N_PARCELAS, IDCATEGORIA, IDFORMA_PAGAMENTO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (self.obtem_dt_registro(), self.obtem_dt_gasto(), self.obtem_valor_gasto(), self.obtem_descricao(), self.obtem_local(), self.verifica_parcelamento(), self.obtem_qtd_parcelas(), self.obtem_categoria(), self.obtem_forma_pagamento())
            )
            connection.commit()
            connection.close()
        else:
            messagebox.showerror("Erro", "Verifique as informações inseridas!")

def main():
    root = tk.Tk()
    app = RegistroDeGastos(root)
    app_relatorios = Gera_relatorio()
    botao_registrar = tk.Button(root, text="Registrar Gasto", command=app.insere_info, borderwidth=4)
    botao_relatorio = tk.Button(root, text="Extrair Relatório", command=app_relatorios.configura_arquivo, borderwidth=4)
    botao_limpar = tk.Button(root, text="Limpar Dados", command=app.limpa_informacoes, borderwidth=4)
    botao_registrar.grid(row=1, column=2, pady=10, padx=(5, 5))
    botao_relatorio.grid(row=3, column=2, pady=10, padx=5)
    botao_limpar.grid(row=5, column=2, pady=10, padx=(5, 10))
    root.mainloop()

if __name__ == "__main__":
    main()