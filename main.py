import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog

try:
    import Impostos
except Exception as e:
    print(f"Aviso: não foi possível importar 'Impostos': {e}. Usando stub de teste.")
    class _StubImpostos:
        @staticmethod
        def calculate_taxes(tipo_atividade, receita_mensal):
            inss = round(receita_mensal * 0.05, 2)
            icms = 0.0
            iss = 0.0
            total = round(inss + icms + iss, 2)
            return {"INSS": inss, "ICMS": icms, "ISS": iss, "Total": total}
    Impostos = _StubImpostos

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
    if not Historico:
        messagebox.showinfo("Histórico", "Nenhuma simulação realizada ainda.", parent=root)
        return
    
    janela_historico = tk.Toplevel(root)
    janela_historico.title("Histórico de Simulações")
    janela_historico.geometry("900x400")
    janela_historico.configure(bg="#1e1e1e")
    
    # Header
    header_frame = tk.Frame(janela_historico, bg="#0d47a1", height=60)
    header_frame.pack(fill="x", padx=0, pady=0)
    header_frame.pack_propagate(False)
    
    title_label = tk.Label(header_frame, text="📋 Histórico de Simulações", 
                          font=("Arial", 18, "bold"), bg="#0d47a1", fg="#FFFFFF")
    title_label.pack(pady=10)
    
    # Criar frame para a tabela
    table_frame = tk.Frame(janela_historico, bg="#1e1e1e")
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Criar Treeview (tabela)
    columns = ("Simulação", "Renda Mensal", "INSS", "ICMS", "ISS", "Total")
    tree = ttk.Treeview(table_frame, columns=columns, height=15, show='headings')
    
    # Definir cabeçalhos
    tree.heading("Simulação", text="Simulação")
    tree.heading("Renda Mensal", text="Renda Mensal")
    tree.heading("INSS", text="INSS")
    tree.heading("ICMS", text="ICMS")
    tree.heading("ISS", text="ISS")
    tree.heading("Total", text="Total")
    
    # Definir largura das colunas
    tree.column("Simulação", width=80, anchor="center")
    tree.column("Renda Mensal", width=140, anchor="center")
    tree.column("INSS", width=100, anchor="center")
    tree.column("ICMS", width=100, anchor="center")
    tree.column("ISS", width=100, anchor="center")
    tree.column("Total", width=100, anchor="center")
    
    # Adicionar dados ao Treeview
    for i, (renda, resultado) in enumerate(Historico, start=1):
        tree.insert("", "end", values=(
            f"#{i}",
            f"R$ {renda:,.2f}",
            f"R$ {resultado.get('INSS', 0):,.2f}",
            f"R$ {resultado.get('ICMS', 0):,.2f}",
            f"R$ {resultado.get('ISS', 0):,.2f}",
            f"R$ {resultado.get('Total', 0):,.2f}"
        ))
    
    # Adicionar scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)
    
    # Frame para botões
    button_frame = tk.Frame(janela_historico, bg="#1e1e1e")
    button_frame.pack(fill="x", padx=10, pady=10)
    
    def limpar_historico():
        if messagebox.askyesno("Confirmar", "Deseja limpar todo o histórico?", parent=janela_historico):
            Historico.clear()
            tree.delete(*tree.get_children())
            messagebox.showinfo("Sucesso", "Histórico limpo!", parent=janela_historico)
    

        
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

