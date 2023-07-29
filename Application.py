import tkinter as tk
from tkinter import ttk, filedialog

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
style.configure('TEntry', font=('Arial', 12), background=bg_color, width=50)
style.configure('TEntry.TEntry', foreground=text_color, show='*')  # Passwort-Eingabe mit Sternchen
style.map('TEntry', foreground=[('focus', text_color)])  # Textfarbe für Eingabe mit Focus (ohne Placeholder)

# Label für private Schlüssel der Vertragspartei 1
private_key_label_1 = ttk.Label(root, text="Privater Schlüssel Vertragspartei 1:")
private_key_label_1.pack(pady=5)

# Eingabefeld für privaten Schlüssel der Vertragspartei 1
private_key_placeholder_1 = "Privater Schlüssel Vertragspartei 1"
private_key_entry_1 = ttk.Entry(root, width=50, show='*')
private_key_entry_1.insert(0, private_key_placeholder_1)
private_key_entry_1.pack(pady=5)

def on_click_entry_1(event):
    if private_key_entry_1.get() == private_key_placeholder_1:
        private_key_entry_1.delete(0, tk.END)
        private_key_entry_1.configure(style='TEntry.TEntry')

def on_leave_entry_1(event):
    if private_key_entry_1.get() == "":
        private_key_entry_1.insert(0, private_key_placeholder_1)
        private_key_entry_1.configure(style='TEntry')

private_key_entry_1.bind('<FocusIn>', on_click_entry_1)
private_key_entry_1.bind('<FocusOut>', on_leave_entry_1)

# Label für private Schlüssel der Vertragspartei 2
private_key_label_2 = ttk.Label(root, text="Privater Schlüssel Vertragspartei 2:")
private_key_label_2.pack(pady=5)

# Eingabefeld für privaten Schlüssel der Vertragspartei 2
private_key_placeholder_2 = "Privater Schlüssel Vertragspartei 2"
private_key_entry_2 = ttk.Entry(root, width=50, show='*')
private_key_entry_2.insert(0, private_key_placeholder_2)
private_key_entry_2.pack(pady=5)

def on_click_entry_2(event):
    if private_key_entry_2.get() == private_key_placeholder_2:
        private_key_entry_2.delete(0, tk.END)
        private_key_entry_2.configure(style='TEntry.TEntry')

def on_leave_entry_2(event):
    if private_key_entry_2.get() == "":
        private_key_entry_2.insert(0, private_key_placeholder_2)
        private_key_entry_2.configure(style='TEntry')

private_key_entry_2.bind('<FocusIn>', on_click_entry_2)
private_key_entry_2.bind('<FocusOut>', on_leave_entry_2)

# Eingabefeld für Dateiauswahl erstellen
file_button = ttk.Button(root, text="Vertrag auswählen", command=submit_text)
file_button.pack(pady=10)

# Button erstellen
submit_button = ttk.Button(root, text="Vertrag speichern", command=submit_text)
submit_button.pack(pady=10)

# Label erstellen, um den eingegebenen Text als Vertrag anzuzeigen
label = ttk.Label(root, text="", anchor='w')
label.pack(pady=20)

# Schleife zum Ausführen des Fensters
root.mainloop()
