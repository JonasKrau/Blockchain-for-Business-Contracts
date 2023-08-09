from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def decrypt_contract(encr_sig_hex, sym_key_hex):
    """
    entschlüsselt signierten Contract
    """
    
    # Umwandlung von Hex in Bytes
    encr_sig = bytes.fromhex(encr_sig_hex)
    sym_key = bytes.fromhex(sym_key_hex)

    # Initialisierungsvektor (IV) extrahieren
    iv = encr_sig[:16]
    encrypted_signature = encr_sig[16:]

    # AES-256-CBC-Entschlüsselung
    cipher = Cipher(algorithms.AES(sym_key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    # Entschlüsselung der Signatur
    decrypted_signature = decryptor.update(encrypted_signature) + decryptor.finalize()

    # Entfernen der Padding
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_signature = unpadder.update(decrypted_signature) + unpadder.finalize()

    return unpadded_signature.hex()


