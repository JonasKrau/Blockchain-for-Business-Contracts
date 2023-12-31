from web3 import Web3
import time
import os


def get_wallet_address():
    # Load wallet address from file
    wallet_address_path = "Data/Wallet/WalletAddress.txt"
    if not os.path.exists(wallet_address_path):
        print("Contract not found.")
        return

    with open(wallet_address_path, 'r', encoding='utf-8') as address_file:
        address_file = address_file.read()

    return address_file


def get_wallet_private_key():
    # Load WalletPrivateKey from file
    wallet_key_path = "Data/Wallet/WalletPrivateKey.txt"
    if not os.path.exists(wallet_key_path):
        print("Contract not found.")
        return

    with open(wallet_key_path, 'r', encoding='utf-8') as contract_file:
        contract_data = contract_file.read()

    return contract_data


def delete_files():
    #The whole secret data will be deleted
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


def write_in_Blockchain(contract_id, encrypted_contract_hex, sig1, sig2, pubkey1, pubkey2):
    web3 = Web3(Web3.HTTPProvider('...')) # Paste here your infura API Key!!!

    address = get_wallet_address()
    address = Web3.to_checksum_address(address)
    private_key = get_wallet_private_key()
    contract_address = '0xFF02dA7f654cd106Be934D2DbBEF888c95176724'
    contract_abi = [
        {
            "anonymous": False,
            "inputs": [
                {"indexed": False, "internalType": "string", "name": "contractId", "type": "string"},
                {"indexed": False, "internalType": "string", "name": "encryptedContract", "type": "string"},
                {"indexed": False, "internalType": "string", "name": "pubkey1", "type": "string"},
                {"indexed": False, "internalType": "string", "name": "pubkey2", "type": "string"},
                {"indexed": False, "internalType": "string", "name": "signature1", "type": "string"},
                {"indexed": False, "internalType": "string", "name": "signature2", "type": "string"}
            ],
            "name": "ContractStored",
            "type": "event"
        },
        {
            "inputs": [{"internalType": "string", "name": "contractId", "type": "string"},
                       {"internalType": "string", "name": "encryptedContract", "type": "string"},
                       {"internalType": "string", "name": "pubkey1", "type": "string"},
                       {"internalType": "string", "name": "pubkey2", "type": "string"},
                       {"internalType": "string", "name": "signature1", "type": "string"},
                       {"internalType": "string", "name": "signature2", "type": "string"}],
            "name": "storeContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    nonce = web3.eth.get_transaction_count(address)
    gas_price = web3.eth.gas_price

    txn_dict = {
		'chainId': 11155111, 
		'nonce': nonce,
		'gas': 2000000,
		'gasPrice': gas_price,  
		'to': contract_address,
		'data': contract.encodeABI(fn_name="storeContract", args=[str(contract_id), encrypted_contract_hex, pubkey1, pubkey2, sig1, sig2]), 
	}


    gas = web3.eth.estimate_gas(txn_dict)
    txn_dict.update({'gas': gas})

    signed = web3.eth.account.sign_transaction(txn_dict, private_key=private_key)

    start = time.time()
    tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)

    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)

    if receipt["status"] == 1:
        print("Wrote successfully")
        end = time.time()
        print(end - start)
    else:
        print("Failed to write")

    delete_files()
