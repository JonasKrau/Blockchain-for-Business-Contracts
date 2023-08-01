import os
import os
from DisplayResults import display_results
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes






def sign_contract():
    """
    Get Signature (signed by both parties) for Contract and return it
    """
    
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
    
    return signature
    #print(signature.hex())


def generate_random_symmetric_key():
    """
    Generate random symmetric key and return it
    """    
    key_length = 32  # 32 Bytes (256-Bit)
    random_key = os.urandom(key_length)
    return random_key



def encrypt_signature_with_symmetric_key():
    signature_bytes = sign_contract()
    symmetric_key_bytes = generate_random_symmetric_key()


    # AES-256-CBC-Verschlüsselung
    iv = os.urandom(16)  # Initialisierungsvektor mit 16 Bytes (AES-256-CBC benötigt 16-Byte-IV)
    cipher = Cipher(algorithms.AES(symmetric_key_bytes), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Die Signatur verschlüsseln und das Ergebnis zurückgeben
    padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_signature = padder.update(signature_bytes) + padder.finalize()
    encrypted_signature = encryptor.update(padded_signature) + encryptor.finalize()
    
    # Symmetrischen Schlüssel und verschlüsselte Signatur in der GUI anzeigen
    encrypted_signature_hex = encrypted_signature.hex()
    symmetric_key_bytes_hex = symmetric_key_bytes.hex()

    relevant_bc_data(symmetric_key_bytes_hex, encrypted_signature_hex)

    

def read_public_keys(file_path):
    """
    Read public keys from the specified file and return a list of public keys.
    Each public key in the list is a string containing the key in PEM format.
    """
    public_keys = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            key_data = file.read()
            key_blocks = key_data.split("-----END PUBLIC KEY-----\n")
            for index, key_block in enumerate(key_blocks):
                if "-----BEGIN PUBLIC KEY-----" in key_block:
                    if index == 1:  # Remove last "-----END PUBLIC KEY-----" only for the second key
                        public_key = key_block + "\n"
                    else:
                        public_key = key_block + "-----END PUBLIC KEY-----\n"
                    public_keys.append(public_key)
    except IOError as e:
        print(f"Error reading public keys: {e}")

    return public_keys


def relevant_bc_data(symmetric_key_bytes_hex, encrypted_signature_hex):
    # Pfade zur Datei mit den öffentlichen Schlüsseln
    public_keys_file_path = "Data/PublicKeys/PublicKeys.txt"

    # Öffentliche Schlüssel aus der Datei laden
    public_keys = read_public_keys(public_keys_file_path)

    # Hier könntest du weitere Verarbeitungsschritte mit den öffentlichen Schlüsseln durchführen,
    # je nachdem, wie du sie verwenden möchtest.
    # In diesem Beispiel gehe ich davon aus, dass die ersten beiden Schlüssel in der Liste relevant sind.
    pubkey1 = public_keys[0] if len(public_keys) > 0 else ""
    pubkey2 = public_keys[1] if len(public_keys) > 1 else ""

        
    # Ergebnisse anzeigen
    display_results(symmetric_key_bytes_hex, encrypted_signature_hex, pubkey1, pubkey2)




