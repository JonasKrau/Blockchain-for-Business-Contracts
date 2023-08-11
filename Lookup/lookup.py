from web3 import Web3
import tkinter as tk
import DecryptVerify



def get_contract_data():
	contract_id = contract_id_entry.get()
	sym_key = sym_key_entry.get()
	encrypted_contract, pubkey1, pubkey2, signature1, signature2 = contract.functions.getContract(contract_id).call()

	print(contract_id)
	print(sym_key)
	print(encrypted_contract)
	print(pubkey1)
	print(pubkey2)
	print(signature1)
	print(signature2)
	

web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/0b9f3b7753854e3482962cf27f6aa40c'))
contract_address = '0xFF02dA7f654cd106Be934D2DbBEF888c95176724'
contract_address = Web3.to_checksum_address(contract_address)
contract_abi = [{"anonymous":False,"inputs":[{"indexed":False,"internalType":"string","name":"contractId","type":"string"},{"indexed":False,"internalType":"string","name":"encryptedContract","type":"string"},{"indexed":False,"internalType":"string","name":"pubkey1","type":"string"},{"indexed":False,"internalType":"string","name":"pubkey2","type":"string"},{"indexed":False,"internalType":"string","name":"signature1","type":"string"},{"indexed":False,"internalType":"string","name":"signature2","type":"string"}],"name":"ContractStored","type":"event"},{"inputs":[{"internalType":"string","name":"contractId","type":"string"}],"name":"getContract","outputs":[{"internalType":"string","name":"encryptedContract","type":"string"},{"internalType":"string","name":"pubkey1","type":"string"},{"internalType":"string","name":"pubkey2","type":"string"},{"internalType":"string","name":"signature1","type":"string"},{"internalType":"string","name":"signature2","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"string","name":"encryptedContract","type":"string"},{"internalType":"string","name":"pubkey1","type":"string"},{"internalType":"string","name":"pubkey2","type":"string"},{"internalType":"string","name":"signature1","type":"string"},{"internalType":"string","name":"signature2","type":"string"}],"name":"storeContract","outputs":[],"stateMutability":"nonpayable","type":"function"}]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# GUI erstellen
root = tk.Tk()
root.option_add('*Font', 'Helvetica 20 bold')
root.title("Get Contract Data")
root.geometry("400x300")

contract_id_label = tk.Label(root, text="Enter Contract ID:")
contract_id_label.pack()

contract_id_entry = tk.Entry(root)
contract_id_entry.pack()

sym_key_label = tk.Label(root, text="Enter Symmetric Key:")
sym_key_label.pack()

sym_key_entry = tk.Entry(root)
sym_key_entry.pack()

get_contract_data_button = tk.Button(root, text="Get Contract Data", command=get_contract_data)
get_contract_data_button.pack()

root.mainloop()



get_contract_data()