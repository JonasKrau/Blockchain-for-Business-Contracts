import tkinter as tk
from tkinter import ttk


def display_results(symmetric_key_hex, encrypted_signature_hex, pubkey1, pubkey2):
    # Neues Fenster erstellen
    result_window = tk.Toplevel()
    result_window.title("Encryption Results")

    # Text-Widget für symmetrischen Schlüssel erstellen
    symmetric_key_text = tk.Text(result_window, wrap=tk.NONE, height=1, padx=5, pady=5)
    symmetric_key_text.insert("1.0", "Symmetric Key: " + symmetric_key_hex)
    symmetric_key_text.pack(pady=5)

    # Text-Widget für verschlüsselte Signatur erstellen
    encrypted_signature_text = tk.Text(result_window, wrap=tk.NONE, height=1, padx=5, pady=5)
    encrypted_signature_text.insert("1.0", "Encrypted Signature: " + encrypted_signature_hex)
    encrypted_signature_text.pack(pady=5)

    # Text-Widget für öffentliche Schlüssel 1 erstellen
    pubkey1_text = tk.Text(result_window, wrap=tk.NONE, height=10, padx=5, pady=5)
    pubkey1_text.insert("1.0", "Public Key 1:\n" + pubkey1)
    pubkey1_text.pack(pady=5)

    # Text-Widget für öffentliche Schlüssel 2 erstellen
    pubkey2_text = tk.Text(result_window, wrap=tk.NONE, height=10, padx=5, pady=5)
    pubkey2_text.insert("1.0", "Public Key 2:" + pubkey2)
    pubkey2_text.pack(pady=5)

    # Funktion zum Markieren und Kopieren des Textes
    def select_text(event):
        event.widget.tag_add("sel", "1.0", "end")

    symmetric_key_text.bind("<Control-a>", select_text)
    encrypted_signature_text.bind("<Control-a>", select_text)
    pubkey1_text.bind("<Control-a>", select_text)
    pubkey2_text.bind("<Control-a>", select_text)



    # Schleife zum Ausführen des Fensters
    result_window.mainloop()
