import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import Impostos

def nova_simulacao():
    # solicita renda mensal (float)
    renda = simpledialog.askfloat("Renda Mensal", "Informe a renda mensal da empresa (R$):",
                                  minvalue=0.0, parent=root)
    if renda is None:
        return  # usuário cancelou
    try:
        # exemplo: chama a função do seu módulo Impostos
        resultado = Impostos.calculate_taxes("Comércio e Serviços", renda)
        if resultado:
            texto = (
                f"Renda mensal: R$ {renda:,.2f}\n\n"
                f"INSS: R$ {resultado.get('INSS', 0):,.2f}\n"
                f"ICMS: R$ {resultado.get('ICMS', 0):,.2f}\n"
                f"ISS: R$ {resultado.get('ISS', 0):,.2f}\n"
                f"Total: R$ {resultado.get('Total', 0):,.2f}"
            )
            messagebox.showinfo("Resultado da Simulação", texto, parent=root)
            Historico.append((renda, resultado))
        else:
            messagebox.showerror("Erro", "Resultado inválido retornado por Impostos.calculate_taxes", parent=root)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o cálculo:\n{e}", parent=root)

def ver_historico():
    
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
    
    simulador.mainloop()

        
Historico = []
# Configuracao da janela principal
root = tk.Tk()
root.title("Simulador de Impostos MEI")
root.geometry("640x360")
root.configure(bg="#1e1e1e")

# Estilo
style = ttk.Style()
style.theme_use('clam')

# ===== HEADER =====
header_frame = tk.Frame(root, bg="#0d47a1", height=80)
header_frame.pack(fill="x", padx=0, pady=0)
header_frame.pack_propagate(False)

title_label = tk.Label(header_frame, text="📊 Simulador de Impostos para MEI", 
                       font=("Arial", 28, "bold"), bg="#0d47a1", fg="#FFFFFF")
title_label.pack(pady=15)

# ===== MENU =====
menu_frame = tk.Frame(root, bg="#2d2d2d", height=50)
menu_frame.pack(fill="x", padx=0, pady=0)
menu_frame.pack_propagate(False)

buttons_menu = ["Nova Simulacao", "Configurações", "Sair"]
for btn_text in buttons_menu:
    btn = tk.Button(menu_frame, text=btn_text, bg="#404040", fg="#FFFFFF",
                    font=("Arial", 11), relief="flat", padx=20, pady=10,
                    activebackground="#505050")
    btn.pack(side="left", padx=5, pady=8)

    if btn_text == "Sair":
        btn.config(command=root.quit)

    if btn_text == "Nova Simulacao":
        btn.config(command=nova_simulacao)

# ===== CONTEÚDO PRINCIPAL =====
content_frame = tk.Frame(root, bg="#1e1e1e")
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Card 1
card1 = tk.Frame(content_frame, bg="#2d2d2d", relief="flat", bd=1)
card1.pack(fill="x", pady=10, ipady=15, ipadx=15)

title_card1 = tk.Label(card1, text="🎯 Bem-vindo!", 
                       font=("Arial", 16, "bold"), bg="#2d2d2d", fg="#4CAF50")
title_card1.pack(anchor="w", pady=(0, 10))

desc_card1 = tk.Label(card1, text="Seja Bem-Vindo ao Simulador de Impostos para Empreendores Independentes.",
                      font=("Arial", 11), bg="#2d2d2d", fg="#cccccc", wraplength=500, justify="left")
desc_card1.pack(anchor="w")

# Card 2 - Botões de ação
card2 = tk.Frame(content_frame, bg="#2d2d2d", relief="flat", bd=1)
card2.pack(fill="x", pady=10, ipady=15, ipadx=15)

title_card2 = tk.Label(card2, text="⚙️ Ações Rápidas",
                       font=("Arial", 16, "bold"), bg="#2d2d2d", fg="#4CAF50")
title_card2.pack(anchor="w", pady=(0, 10))

button_frame = tk.Frame(card2, bg="#2d2d2d")
button_frame.pack(anchor="w")

actions = ["Novo Relatório", "Ver Histórico", "Exportar"]
for action in actions:
    action_btn = tk.Button(button_frame, text=action, bg="#4CAF50", fg="white",
                           font=("Arial", 10, "bold"), relief="flat", padx=15, pady=8,
                           activebackground="#45a049")
    action_btn.pack(side="left", padx=5)
    if action == "Novo Relatório":
        action_btn.config(command=nova_simulacao)
    elif action == "Ver Histórico":
        def ver_historico():
            if not Historico:
                messagebox.showinfo("Histórico", "Nenhuma simulação realizada ainda.", parent=root)
                return
            hist_text = ""
            for i, (renda, resultado) in enumerate(Historico, start=1):
                hist_text += (f"Simulação {i}:\n"
                              f" Renda Mensal: R$ {renda:,.2f}\n"
                              f" INSS: R$ {resultado.get('INSS', 0):,.2f}, "
                              f"ICMS: R$ {resultado.get('ICMS', 0):,.2f}, "
                              f"ISS: R$ {resultado.get('ISS', 0):,.2f}, "
                              f"Total: R$ {resultado.get('Total', 0):,.2f}\n\n")
            messagebox.showinfo("Histórico de Simulações", hist_text, parent=root)
        action_btn.config(command=ver_historico)

# ===== FOOTER =====
footer_frame = tk.Frame(root, bg="#0d47a1", height=40)
footer_frame.pack(fill="x", side="bottom")
footer_frame.pack_propagate(False)

footer_label = tk.Label(footer_frame, text="© 2025 Simulador de Impostos MEI - Todos os direitos reservados",
                        font=("Arial", 9), bg="#0d47a1", fg="#FFFFFF")
footer_label.pack(pady=10)

print("Application started sucessfully.")

root.mainloop()

