import os
import tkinter as tk
from tkinter import ttk, filedialog

def toggle_show_hide(entry_widget, lock_button):
    if entry_widget.cget("show") == "":
        entry_widget.configure(show="*")
        lock_button.config(text="Verbergen/Anzeigen")
    else:
        entry_widget.configure(show="")
        lock_button.config(text="Verbergen/Anzeigen")

def submit_text():
    # Vertrag aus Datei laden
    file_path = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
    if not file_path:
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        contract_data = file.read()
    
    # Private Keys der Vertragsparteien
    private_key_1 = private_key_entry_1.get()
    private_key_2 = private_key_entry_2.get()

    # Hier könntest du den Vertrag mit den privaten Schlüsseln weiterverarbeiten oder anzeigen
    label.config(text="Eingegebener Vertrag:\n" + contract_data)

    # Vertrag in Data speichern
    data_directory = "Data"
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    contract_filename = os.path.join(data_directory, 'contract.txt')
    with open(contract_filename, 'w', encoding='utf-8') as contract_file:
        contract_file.write(contract_data)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Vertrags-GUI")

# Farben definieren
bg_color = '#f9f9f9'  # Hintergrundfarbe
text_color = '#333333'  # Textfarbe
button_color = '#4CAF50'  # Button-Farbe
button_text_color = 'white'  # Button-Textfarbe

# Styles für das Design definieren
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), foreground=text_color, background=bg_color, wraplength=600, justify='left')
style.configure('TEntry', font=('Arial', 12), background=bg_color, width=50, show="*")  # Eingabe mit Verbergen
style.map('TEntry', foreground=[('focus', text_color)])  # Textfarbe für Eingabe mit Focus (ohne Placeholder)

# Label für private Schlüssel der Vertragspartei 1
private_key_label_1 = ttk.Label(root, text="Privater Schlüssel Vertragspartei 1:")
private_key_label_1.pack(pady=5)

# Eingabefeld für privaten Schlüssel der Vertragspartei 1
private_key_entry_1 = ttk.Entry(root)
private_key_entry_1.pack(pady=5)

# Lock-Button für privaten Schlüssel der Vertragspartei 1
lock_button_1 = ttk.Button(root, text="Verbergen", command=lambda: toggle_show_hide(private_key_entry_1, lock_button_1))
lock_button_1.pack()

# Label für private Schlüssel der Vertragspartei 2
private_key_label_2 = ttk.Label(root, text="Privater Schlüssel Vertragspartei 2:")
private_key_label_2.pack(pady=5)

# Eingabefeld für privaten Schlüssel der Vertragspartei 2
private_key_entry_2 = ttk.Entry(root)
private_key_entry_2.pack(pady=5)

# Lock-Button für privaten Schlüssel der Vertragspartei 2
lock_button_2 = ttk.Button(root, text="Verbergen", command=lambda: toggle_show_hide(private_key_entry_2, lock_button_2))
lock_button_2.pack()

# Eingabefeld für Dateiauswahl erstellen
file_button = ttk.Button(root, text="Vertrag auswählen", command=submit_text)
file_button.pack(pady=10)

# Button erstellen
submit_button = ttk.Button(root, text="Vertrag signieren", command=submit_text)
submit_button.pack(pady=10)

# Label erstellen, um den eingegebenen Text als Vertrag anzuzeigen
label = ttk.Label(root, text="", anchor='w')
label.pack(pady=20)

# Schleife zum Ausführen des Fensters
root.mainloop()
