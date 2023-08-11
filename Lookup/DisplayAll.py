import tkinter as tk

def display_contract(decrypted_contract):
    # Erstellen des Hauptfensters
    root = tk.Tk()
    root.option_add('*Font', 'Helvetica 20 bold')
    root.title('Decrypted Contract')

    # Erstellen eines Labels, um die erfolgreiche Verifizierungsnachricht anzuzeigen
    verification_label = tk.Label(root, text="Signatures have been verified successfully!", wraplength=800, fg="green")
    verification_label.pack()

    # Erstellen eines Labels für die Überschrift "Decrypted Contract:"
    contract_heading = tk.Label(root, text="Decrypted Contract:", font='Helvetica 18')
    contract_heading.pack()

    # Erstellen eines Textwidgets, um den Vertrag anzuzeigen
    text_widget = tk.Text(root, wrap=tk.WORD, font='Helvetica 14')
    text_widget.pack(expand=tk.YES, fill=tk.BOTH)

    # Hinzufügen des entschlüsselten Vertrags zum Textwidget
    text_widget.insert(tk.END, decrypted_contract)

    # Hauptereignisschleife ausführen
    root.mainloop()
