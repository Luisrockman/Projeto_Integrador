import tkinter as tk
from tkinter import ttk

simulador = tk.Tk()
simulador.title("Módulo de Impostos MEI")
simulador.geometry("640x360")
simulador.configure(bg="#1e1e1e")
simulador.resizable(True,True)

style = ttk.Style()
style.theme_use('clam')

header_frame = tk.Frame(simulador, bg="#0d47a1", height=80)
header_frame.pack(fill="x", padx=0, pady=0)
header_frame.pack_propagate(False)

def calculate_taxes(tipo_atividade, receita_mensal):
    INSS = 75.90
    ISS = 5.00
    ICMS = 1.00

    if tipo_atividade == "Comércio":
        inss = receita_mensal * 0.05
        icms = ICMS
        total = inss + icms
    elif tipo_atividade == "Serviços":
        inss = receita_mensal * 0.05
        iss = ISS
        total = inss + iss
    elif tipo_atividade == "Comércio e Serviços":
        inss = receita_mensal * 0.05
        icms = ICMS
        iss = ISS
        total = inss + icms + iss
    else:
        return None

    return {
        "INSS": round(inss, 2),
        "ICMS": round(icms, 2) if 'icms' in locals() else 0,
        "ISS": round(iss, 2) if 'iss' in locals() else 0,
        "Total": round(total, 2)
    }

simulador.mainloop()