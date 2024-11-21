import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

class App_Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Financeiro")
        self.root.geometry("800x600")
        
        self.frame_resumo = tk.Frame(self.root, bg="lightblue")
        self.frame_resumo.pack(fill="x", padx=10, pady=10)
        
        self.painel_resumoDashboard()
    
    def painel_resumoDashboard(self):
        
        label_gasto_total = tk.Label(self.frame_resumo, text="2500,00R$", font=("Arial", 12))
        label_gasto_total.grid(row=1, column=1)

    

# Inicializando a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App_Dashboard(root)
    root.mainloop()