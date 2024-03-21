import tkinter as tk
from tkinter import ttk
import math

def calcular_pH(concentracao_acido, Ka):
    log_concentracao = -math.log10(concentracao_acido)
    log_Ka = -math.log10(Ka)
    pH = log_Ka + log_concentracao
    return pH

tabela_acidos = {
    "CH3COOH": {"Ka": 1.8e-5},
    "HCN": {"Ka": 4.9e-10},
    "H2S": {"Ka": 9.1e-8},
    "HCOOH": {"Ka": 1.8e-4},
    "HF": {"Ka": 6.8e-4},
    "C6H5COOH": {"Ka": 6.3e-5},
    "C6H8O7": {"Ka": 7.5e-4},
    "C3H6O3": {"Ka": 1.4e-4},
    "C4H6O6": {"Ka": 1.0e-4},
    "C2H4O2": {"Ka": 1.8e-5},
    "H2CO3": {"Ka": 4.3e-7}
}

def calcular_pH_button():
    acid = acid_entry.get()
    concentration_str = concentration_entry.get()

    try:
        concentration = float(concentration_str)
    except ValueError:
        result_label.config(text="Erro: Concentração inválida.")
        return

    if acid in tabela_acidos:
        Ka = tabela_acidos[acid]["Ka"]
        pH = calcular_pH(concentration, Ka)
        result_label.config(text="O pH do ácido {} é: {:.2f}".format(acid, pH))
    else:
        result_label.config(text="Ácido não encontrado na tabela.")

def fill_acid_entry(event):
    selected_acid = acid_listbox.get(acid_listbox.curselection())
    acid_entry.delete(0, tk.END)
    acid_entry.insert(0, selected_acid)

# Create the main window
window = tk.Tk()
window.title("pH Calculator")

# Create and place the acid label and entry
acid_label = tk.Label(window, text="Ácido:")
acid_label.pack()
acid_entry = tk.Entry(window)
acid_entry.pack()

# Create and place the concentration label and entry with placeholder text and explanation
concentration_label = tk.Label(window, text="Concentração (em mol/L, use notação científica '10^x' como '1.0e-3'):")
concentration_label.pack()
concentration_entry = ttk.Entry(window, width=30)
concentration_entry.insert(0, "Digite a concentração")
concentration_entry.pack()

# Function to handle focus in event
def on_entry_click(event):
    if concentration_entry.get() == "Digite a concentração":
        concentration_entry.delete(0, tk.END)
        concentration_entry.config(foreground='black')

# Function to handle focus out event
def on_focus_out(event):
    if not concentration_entry.get():
        concentration_entry.insert(0, "Digite a concentração")
        concentration_entry.config(foreground='grey')

# Bind events to entry widget
concentration_entry.bind('<FocusIn>', on_entry_click)
concentration_entry.bind('<FocusOut>', on_focus_out)

# Create and place the calculate button
calculate_button = tk.Button(window, text="Calcular pH", command=calcular_pH_button)
calculate_button.pack()

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Create and place the acid table
table_label = tk.Label(window, text="Ácidos disponíveis:")
table_label.pack()

acid_listbox = tk.Listbox(window)
acid_listbox.pack()

for acid in tabela_acidos:
    acid_listbox.insert(tk.END, acid)

# Bind double click event to fill acid entry
acid_listbox.bind("<Double-Button-1>", fill_acid_entry)

# Start the GUI event loop
window.mainloop()
