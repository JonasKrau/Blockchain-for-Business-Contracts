from web3 import Web3
import time

def write_in_Blockchain(contract_id, encrypted_signature_hex, pubkey1, pubkey2):
    web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/0b9f3b7753854e3482962cf27f6aa40c'))

    address = '..........' #Walletaddress (muss in DisplayResults in GUI eingegeben werde!!!)
    private_key = '.........' #Private Key from Contract (muss in DisplayResults in GUI eingegeben werde!!!)
    contract_address = '0xC5fb728194F843061479ddFDe12106A667052a1e'
    contract_abi = [{"inputs":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"string","name":"encryptedSignature","type":"string"},{"internalType":"string","name":"pubkey1","type":"string"},{"internalType":"string","name":"pubkey2","type":"string"}],"name":"storeContract","outputs":[],"stateMutability":"nonpayable","type":"function"}]

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
