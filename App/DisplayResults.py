import uuid
import tkinter as tk
import WriteBlockchain


def display_results(sym_key_hex, encrypted_contract, sig1, sig2, pubkey1, pubkey2):

    # Create Window
    root = tk.Tk()
    root.option_add('*Font', 'Helvetica 20 bold')
    root.title('Results')

    # Create UUID
    contract_id = uuid.uuid4()

    # widgets for displaying UUID, sym_key_hex and encrypted_contract
    label1 = tk.Label(root, text="Contract-ID:")
    label1.pack()
    text1 = tk.Text(root, height=1, width=40)
    text1.insert(tk.END, str(contract_id))
    text1.pack()

    label2 = tk.Label(root, text="Symmetric Key:")
    label2.pack(pady=(20,1))
    text2 = tk.Text(root, height=1, width=60)
    text2.insert(tk.END, sym_key_hex)
    text2.pack()

    # Description of symmetric key
    warning_label = tk.Label(root, text="Store the key at a safe place!", fg="red")
    warning_label.pack()

    label3 = tk.Label(root, text="Encrypted Contract:")
    label3.pack(pady=(20,1))
    text3 = tk.Text(root, height=4, width=60)
    text3.insert(tk.END, encrypted_contract)
    text3.pack()

    # Button, for storing the data in Ethereum Sepolia Blockchain
    store_button = tk.Button(root, text="Store in Sepolia Blockchain", command=lambda:WriteBlockchain.write_in_Blockchain(str(contract_id), encrypted_contract, sig1, sig2, pubkey1, pubkey2 ))
    store_button.pack(pady=(100,5))

    # Descrption of what will happen, after pressing the Button
    description_label = tk.Label(root, text="When pressing the button, the contract ID, the encrypted contract, the two signatures and the two entered public keys are stored in the Ethereum Sepolia Blockchain.", wraplength=600, fg="red")
    description_label.pack(pady=(5,20))

    # Loop
    root.mainloop()
