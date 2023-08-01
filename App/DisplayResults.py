import tkinter as tk
from tkinter import ttk
import WriteBlockchain



def display_results(symmetric_key_hex, encrypted_signature_hex, pubkey1, pubkey2):
    # Neues Fenster erstellen
    result_window = tk.Toplevel()
    result_window.title("Blockchain for Business-Contracts: Results")

    # Text-Widget für symmetrischen Schlüssel erstellen
    symmetric_key_text = tk.Text(result_window, wrap=tk.NONE, height=1, padx=5, pady=5)
    symmetric_key_text.insert("1.0", "Symmetric Key: " + symmetric_key_hex)
    symmetric_key_text.pack(pady=5)

    # Beschreibung des symmetrischen Schlüssels
    symmetric_key_description = tk.Label(result_window, text="This is the randomly generated symmetric key. Keep it safe!", font=("Helvetica", 12))
    symmetric_key_description.pack(pady=(0, 20))

    # Text-Widget für verschlüsselte Signatur erstellen
    encrypted_signature_text = tk.Text(result_window, wrap=tk.NONE, height=1, padx=5, pady=5)
    encrypted_signature_text.insert("1.0", "Signed and Encrypted Contract: " + encrypted_signature_hex)
    encrypted_signature_text.pack(pady=5)

    # Beschreibung der verschlüsselten Signatur
    encrypted_signature_description = tk.Label(result_window, text="The contract was signed with both private keys and then encrypted with the randomly generated symmetric key. First party 1 has signed, then party 2.", font=("Helvetica", 12))
    encrypted_signature_description.pack(pady=(0, 20))

    # Text-Widget für öffentliche Schlüssel 1 erstellen
    pubkey1_text = tk.Text(result_window, wrap=tk.NONE, height=8, padx=5, pady=5)
    pubkey1_text.insert("1.0", "Public Key 1:\n" + pubkey1)
    pubkey1_text.pack(pady=5)

    # Beschreibung von öffentlichem Schlüssel 2
    pubkey1_description = tk.Label(result_window, text="This is the public key of contract party 1.", font=("Helvetica", 12))
    pubkey1_description.pack(pady=(0, 20))

    # Text-Widget für öffentliche Schlüssel 2 erstellen
    pubkey2_text = tk.Text(result_window, wrap=tk.NONE, height=8, padx=5, pady=5)
    pubkey2_text.insert("1.0", "Public Key 2:" + pubkey2)
    pubkey2_text.pack(pady=5)

    #Beschreibung von öffentlichem Schlüssel 2
    pubkey2_description = tk.Label(result_window, text="This is the public key of contract party 2.", font=("Helvetica", 12))
    pubkey2_description.pack(pady=(0, 20))

    # Funktion zum Markieren und Kopieren des Textes
    def select_text(event):
        event.widget.tag_add("sel", "1.0", "end")

    symmetric_key_text.bind("<Control-a>", select_text)
    encrypted_signature_text.bind("<Control-a>", select_text)
    pubkey1_text.bind("<Control-a>", select_text)
    pubkey2_text.bind("<Control-a>", select_text)




    # Button zum Speichern in die Blockchain
    write_to_blockchain_button = ttk.Button(result_window, text="Write in to Blockchain", command=lambda: WriteBlockchain.write_in_Blockchain(encrypted_signature_hex, pubkey1, pubkey2))
    write_to_blockchain_button.pack(pady=10)

    
    
    # Beschreibung des Buttons als kleines Label
    description_label = tk.Label(result_window, text="By pressing this button, the two public keys and the contract (signed and encrypted) are stored in the blockchain. ", font=("Helvetica", 12))
    description_label.pack(pady=(1, 20))

  
    # Schleife zum Ausführen des Fensters
    result_window.mainloop()
