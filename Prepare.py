import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def sign_contract():
    # Contract aus Datei laden
    contract_path = "Data/Contract/contract.txt"
    if not os.path.exists(contract_path):
        print("Contract not found.")
        return

    with open(contract_path, 'r', encoding='utf-8') as contract_file:
        contract_data = contract_file.read()

    # Private Keys aus Datei laden
    private_keys_path = "Data/PrivateKeys/PrivateKeys.txt"
    if not os.path.exists(private_keys_path):
        print("Private Keys not found.")
        return

    private_keys = []
    with open(private_keys_path, 'r', encoding='utf-8') as keys_file:
        key_data = keys_file.read()
        key_blocks = key_data.split("\n\n")
        for key_block in key_blocks:
            private_key = serialization.load_pem_private_key(
                key_block.encode('utf-8'),
                password=None,
                backend=default_backend()
            )
            private_keys.append(private_key)

    # Signieren des Contracts mit den Private Keys
    signature = None
    for private_key in private_keys:
        if signature is None:
            signature = private_key.sign(
                contract_data.encode('utf-8'),
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
        else:
            signature = private_key.sign(
                signature,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )

    # Die finale Signatur ausgeben)
    
    return signature.hex()
    #print(signature.hex())

