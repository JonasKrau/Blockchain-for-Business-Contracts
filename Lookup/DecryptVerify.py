from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import DisplayAll


def decrypt_verify_data(encrypted_contract, pubkey1, pubkey2, signature1, signature2, sym_key):
    print("Retrieved Contract Data")
    print("---------------------------------------------------------------------------\n\n")
    print("Encrypted Contract:\n", encrypted_contract)
    print("\nPublic Key (Party 1):\n", pubkey1)
    print("Public Key (Party 2):", pubkey2)
    print("Signature (Party 1):\n", signature1)
    print("\nSignature (Party 2):\n", signature2)

    try:
        # Load Public Keys
        public_key1 = load_pem_public_key(pubkey1.encode(), backend=default_backend())
        public_key2 = load_pem_public_key(pubkey2.encode(), backend=default_backend())

        # Verify first signature
        public_key1.verify(
            bytes.fromhex(signature1),
            encrypted_contract.encode('utf-8'),
            asym_padding.PSS(mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )

        # Verify second signature
        public_key2.verify(
            bytes.fromhex(signature2),
            encrypted_contract.encode('utf-8'),
            asym_padding.PSS(mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("\n\n\nDecryption and Verification")
        print("---------------------------------------------------------------------------")
        print("\nSignature verification successful\n")

        # Convert the symmetric key into bytes
        symmetric_key_bytes = bytes.fromhex(sym_key)

        # Convert the encrypted contract into bytes
        encrypted_contract_bytes = bytes.fromhex(encrypted_contract)

        # Create Cipher Object (ECB-Modus)
        cipher = Cipher(algorithms.AES(symmetric_key_bytes), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt data
        decrypted_data_padded = decryptor.update(encrypted_contract_bytes) + decryptor.finalize()

        # Delete Paddings (PKCS7)
        unpadder = sym_padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_data_padded) + unpadder.finalize()

        # Print Decoded contract data
        print("\nDecrypted Contract:\n", decrypted_data.decode('utf-8'))
        DisplayAll.display_contract(decrypted_data.decode('utf-8'))

    except InvalidSignature:
        print("Verification failed. The signatures do not match the encrypted contract.")
    
    

    
