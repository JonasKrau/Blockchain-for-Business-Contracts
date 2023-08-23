from DisplayResults import display_results
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
import os


def generate_random_symmetric_key():
    """
    Generates random symmetric key and return it
    """    
    key_length = 32  # 32 Bytes (256-Bit)
    random_key = os.urandom(key_length)
    return random_key


def encrypt_contract(symmetric_key):
    
    # load contract from file
    contract_path = "Data/Contract/contract.txt"
    if not os.path.exists(contract_path):
        print("Contract not found.")
        return None

    with open(contract_path, 'r', encoding='utf-8') as contract_file:
        contract_data = contract_file.read()

    # Padder for AES-Blocksize (128-Bit)
    padder = sym_padding.PKCS7(128).padder()
    padded_data = padder.update(contract_data.encode('utf-8')) + padder.finalize()

    # Create Cipher Object (ECB-Modus)
    cipher = Cipher(algorithms.AES(symmetric_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt Data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data.hex()

 
def sign_contract_party1(encr_contract):
    """
    Get Signature of Party1
    """
    # Load Private Keys from file
    private_keys_path = "Data/PrivateKeys/PrivateKeys.txt"
    if not os.path.exists(private_keys_path):
        print("Private Keys not found.")
        return

    with open(private_keys_path, 'r', encoding='utf-8') as keys_file:
        key_data = keys_file.read()
        key_blocks = key_data.split("\n\n")
        private_key = serialization.load_pem_private_key(
            key_blocks[0].encode('utf-8'),
            password=None,
            backend=default_backend()
        )

    # Sign Contract with first Private Key
    signature = private_key.sign(
        encr_contract.encode('utf-8'),
        asym_padding.PSS(mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    # return signature
    return signature.hex()
    #print(signature.hex())



def sign_contract_party2(encr_contract):
    """
    Get Signature of Party2
    """
    # Load Private Key from file
    private_keys_path = "Data/PrivateKeys/PrivateKeys.txt"
    if not os.path.exists(private_keys_path):
        print("Private Keys not found.")
        return

    with open(private_keys_path, 'r', encoding='utf-8') as keys_file:
        key_data = keys_file.read()
        key_blocks = key_data.split("\n\n")
        if len(key_blocks) < 2:
            print("Second private key not found.")
            return
        private_key = serialization.load_pem_private_key(
            key_blocks[1].encode('utf-8'),
            password=None,
            backend=default_backend()
        )

    # Sign contract with second Private Key
    signature = private_key.sign(
        encr_contract.encode('utf-8'),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    # return Signature
    return signature.hex()
    #print(signature.hex())


def read_public_keys():
    """
    Read public keys from the specified file and return a list of public keys.
    Each public key in the list is a string containing the key in PEM format.
    """
    public_keys = []

    file_path = "Data/PublicKeys/PublicKeys.txt"

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


def order_data():

    sym_key = generate_random_symmetric_key()
    encrypted_contract = encrypt_contract(sym_key)
    sig1 = sign_contract_party1(encrypted_contract)
    sig2 = sign_contract_party2(encrypted_contract)
    pubkeys = read_public_keys()
    pubkey1= pubkeys[0]
    pubkey2= pubkeys[1]

    sym_key_hex = sym_key.hex()

    display_results(sym_key_hex, encrypted_contract, sig1, sig2, pubkey1, pubkey2)
