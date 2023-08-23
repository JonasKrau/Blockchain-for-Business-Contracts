import os
import tkinter as tk
from tkinter import ttk, filedialog
import Prepare


def toggle_show_hide(entry_widget, lock_button):
    if entry_widget.cget("show") == "":
        entry_widget.configure(show="*")
        lock_button.config(state="disabled")  # Disables the "Show" button
    else:
        entry_widget.configure(show="")
        lock_button.config(state="disabled")  # Disables the "Hide" button after displaying the text




def submit_text():
    # Vertrag aus Datei laden
    file_path = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
    if not file_path:
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        contract_data = file.read()
    
    # Private Keys of the Contracting Parties
    private_key_1 = private_key_entry_1.get()
    private_key_2 = private_key_entry_2.get()

    # Public Keys of the Contracting Parties
    public_key_1 = public_key_entry_1.get()
    public_key_2 = public_key_entry_2.get()

    wallet_address = wallet_address_entry.get()
    wallet_private_key = wallet_private_key_entry.get()
    

   
    #label.config(text="Contract:\n" + contract_data)

    # Save contract in Data
    data_directory = "Data/Contract"
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    contract_filename = os.path.join(data_directory, 'contract.txt')
    with open(contract_filename, 'w', encoding='utf-8') as contract_file:
        contract_file.write(contract_data)

    # Save private keys to file
    keys_directory = "Data/PrivateKeys"
    if not os.path.exists(keys_directory):
        os.makedirs(keys_directory)

    keys_filename = os.path.join(keys_directory, 'PrivateKeys.txt')
    with open(keys_filename, 'w', encoding='utf-8') as keys_file:
        keys_file.write(private_key_1 + "\n\n" + private_key_2)  # Hier werden die beiden privaten Schlüssel mit zwei Leerzeilen getrennt

    # Save public keys to file
    public_keys_directory = "Data/PublicKeys"
    if not os.path.exists(public_keys_directory):
        os.makedirs(public_keys_directory)

    public_keys_filename = os.path.join(public_keys_directory, 'PublicKeys.txt')
    with open(public_keys_filename, 'w', encoding='utf-8') as public_keys_file:
        public_keys_file.write(public_key_1 + "\n\n" + public_key_2)  # Hier werden die beiden öffentlichen Schlüssel mit zwei Leerzeilen getrennt

     
    # Save wallet address to file
    wallet_directory = "Data/Wallet"
    if not os.path.exists(wallet_directory):
        os.makedirs(wallet_directory)

    wallet_filename = os.path.join(wallet_directory, 'WalletAddress.txt')
    with open(wallet_filename, 'w', encoding='utf-8') as wallet_file:
        wallet_file.write(wallet_address)

    # Save private key of wallet address to file
    wallet_private_key_filename = os.path.join(wallet_directory, 'WalletPrivateKey.txt')
    with open(wallet_private_key_filename, 'w', encoding='utf-8') as wallet_private_key_file:
        wallet_private_key_file.write(wallet_private_key)


# Create main window
root = tk.Tk()
root.option_add('*Font', 'Helvetica 20 bold')

root.title("Blockchain for Business Contracts: Start")

# Define colors
bg_color = '#f9f9f9'  # Hintergrundfarbe
text_color = '#333333'  # Textfarbe
button_color = '#4CAF50'  # Button-Farbe
button_text_color = 'white'  # Button-Textfarbe

# Define styles for the design
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 20, 'bold'), foreground=text_color, background=bg_color, wraplength=600, justify='left')
style.configure('TEntry', font=('Helvetica', 20, 'bold'), background=bg_color, width=50, show="*")  # Eingabe mit Verbergen
style.map('TEntry', foreground=[('focus', text_color)])  # Textfarbe für Eingabe mit Focus (ohne Placeholder)

# Party 1 private key label
private_key_label_1 = ttk.Label(root, text="Private Key (Party 1):")
private_key_label_1.pack(pady=10)

# Input field for private key of contracting party 1
private_key_entry_1 = ttk.Entry(root)
private_key_entry_1.pack(pady=10)

# Lock button for private key of the contracting party 1
lock_button_1 = ttk.Button(root, text="Hide", command=lambda: toggle_show_hide(private_key_entry_1, lock_button_1))
lock_button_1.pack()

# Party 1 public key label
public_key_label_1 = ttk.Label(root, text="Public Key (Party 1):")
public_key_label_1.pack(pady=(40, 10))

# Input field for public key of contracting party 1
public_key_entry_1 = ttk.Entry(root)
public_key_entry_1.pack(pady=10)

# Party 2 private key label
private_key_label_2 = ttk.Label(root, text="Private Key (Party 2):")
private_key_label_2.pack(pady=(40,10))

# Input field for private key of contracting party 2
private_key_entry_2 = ttk.Entry(root)
private_key_entry_2.pack(pady=5)

# Lock button for private key of the contracting party 2
lock_button_2 = ttk.Button(root, text="Hide", command=lambda: toggle_show_hide(private_key_entry_2, lock_button_2))
lock_button_2.pack()

# Party 2 public key label
public_key_label_2 = ttk.Label(root, text="Public Key (Party 2):")
public_key_label_2.pack(pady=(40, 10))

# Input field for public key of the contracting party 2
public_key_entry_2 = ttk.Entry(root)
public_key_entry_2.pack(pady=5)

# Label for wallet address
wallet_address_label = ttk.Label(root, text="Wallet Address:")
wallet_address_label.pack(pady=(40, 10))

# Input field for wallet address
wallet_address_entry = ttk.Entry(root)
wallet_address_entry.pack(pady=5)

# Label for private key of wallet address
wallet_private_key_label = ttk.Label(root, text="Private Key for Wallet Address:")
wallet_private_key_label.pack(pady=(40, 10))

# Input field for private key of wallet address
wallet_private_key_entry = ttk.Entry(root)
wallet_private_key_entry.pack(pady=5)

# Lock button for private key of wallet address
wallet_lock_button = ttk.Button(root, text="Hide", command=lambda: toggle_show_hide(wallet_private_key_entry, wallet_lock_button))
wallet_lock_button.pack()

# Create input field for file selection
file_button = ttk.Button(root, text="Select Contract", command=submit_text)
file_button.pack(pady=(40,10))

# Create button
submit_button = ttk.Button(root, text="Sign & Encrypt Contract", command=Prepare.order_data)
submit_button.pack(pady=10)


# Loop to run the window
root.mainloop()
