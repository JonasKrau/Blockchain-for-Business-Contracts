from web3 import Web3
import time
import os

def get_wallet_address():
    #WalletAddresse aus Datei laden
    wallet_address_path = "Data/Wallet/WalletAddress.txt"
    if not os.path.exists(wallet_address_path):
        print("Contract not found.")
        return

    with open(wallet_address_path, 'r', encoding='utf-8') as address_file:
        address_file = address_file.read()

    return address_file


def get_wallet_private_key():
    #WalletPrivateKey aus Datei laden
    wallet_key_path = "Data/Wallet/WalletPrivateKey.txt"
    if not os.path.exists(wallet_key_path):
        print("Contract not found.")
        return

    with open(wallet_key_path, 'r', encoding='utf-8') as contract_file:
        contract_data = contract_file.read()

    return contract_data



def delete_files():
    #Hier werden die ganzen/gehimen Daten gelöscht
    files_to_delete = [
        "Data/Contract/contract.txt",
        "Data/PrivateKeys/PrivateKeys.txt",
        "Data/PublicKeys/PublicKeys.txt",
        "Data/Wallet/WalletAddress.txt",
        "Data/Wallet/WalletPrivateKey.txt",
    ]
    
    for file_path in files_to_delete:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {file_path} has been deleted.")
        else:
            print(f"File {file_path} does not exist.")




def write_in_Blockchain(contract_id, encrypted_signature_hex, pubkey1, pubkey2):
    web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/0b9f3b7753854e3482962cf27f6aa40c'))

    address = get_wallet_address()
    address = Web3.to_checksum_address(address)
    private_key = get_wallet_private_key()
    contract_address = '0x9762417DC27F8a20EcdB350A22DD50b5e6E3644E' #Contract oder Walletadresse!!!!!!!!!!!!!!!!?????????????????
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

    nonce = web3.eth.get_transaction_count(address)
    gas_price = web3.eth.gas_price  # Aktuellen Gaspreis abrufen

    txn_dict = {
        'chainId': 11155111, # Anpassen, wenn du ein anderes Netzwerk verwendest
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': gas_price,  # Gaspreis hinzufügen
        'to': contract_address,
        'data': contract.encodeABI(fn_name="storeContract", args=[contract_id, encrypted_signature_hex, pubkey1, pubkey2]),
    }

    # Gas schätzen
    gas = web3.eth.estimate_gas(txn_dict)
    txn_dict.update({'gas': gas})

    # Transaktion signieren
    signed = web3.eth.account.sign_transaction(txn_dict, private_key=private_key)

    # Transaktion senden
    start = time.time()
    tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)

    # Warten, bis die Transaktion abgebaut wurde
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)

    # Überprüfung des Transaktionsstatus
    if receipt["status"] == 1:
        print("Wrote successfully")
        end = time.time()
        print(end-start)
    else:
        print("Failed to write")

    delete_files()
