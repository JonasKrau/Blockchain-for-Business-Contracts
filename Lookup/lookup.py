from web3 import Web3
import tkinter as tk

def get_contract_data():
    contract_id = contract_id_entry.get()
    encrypted_signature, pubkey1, pubkey2 = contract.functions.getContract(contract_id).call()
    print(f"Contract ID: {contract_id}")
    print(f"Encrypted Signature: {encrypted_signature}")
    print(f"Pubkey 1: {pubkey1}")
    print(f"Pubkey 2: {pubkey2}")

web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/0b9f3b7753854e3482962cf27f6aa40c'))
contract_address = '0x9762417DC27F8a20EcdB350A22DD50b5e6E3644E'
contract_address = Web3.to_checksum_address(contract_address)
contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "contractId",
                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "encryptedSignature",
                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "pubkey1",
                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "pubkey2",
                "type": "string"
            }
        ],
        "name": "ContractStored",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "contractId",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "encryptedSignature",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "pubkey1",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "pubkey2",
                "type": "string"
            }
        ],
        "name": "storeContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "contractId",
                "type": "string"
            }
        ],
        "name": "getContract",
        "outputs": [
            {
                "internalType": "string",
                "name": "encryptedSignature",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "pubkey1",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "pubkey2",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# GUI erstellen
root = tk.Tk()
root.option_add('*Font', 'Helvetica 20 bold')
root.title("Get Contract Data")
root.geometry("400x200")

contract_id_label = tk.Label(root, text="Enter Contract ID:")
contract_id_label.pack()

contract_id_entry = tk.Entry(root)
contract_id_entry.pack()

get_contract_data_button = tk.Button(root, text="Get Contract Data", command=get_contract_data)
get_contract_data_button.pack()

root.mainloop()
