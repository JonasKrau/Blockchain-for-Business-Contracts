from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def decrypt_verify_data(encrypted_contract, pubkey1, pubkey2, signature1, signature2, sym_key):
    print("Retrieved Contract Data\n")
    print("--------------------------------------------------------------\n\n\n")
    print("Encrypted Contract:\n", encrypted_contract)
    print("\nPublic Key (Party 1):\n", pubkey1)
    print("Public Key (Party 2):", pubkey2)
    print("Signature (Party 1):\n", signature1)
    print("\nSignature (Party 2):\n", signature2)

    try:
        # Lade die öffentlichen Schlüssel
        public_key1 = load_pem_public_key(pubkey1.encode(), backend=default_backend())
        public_key2 = load_pem_public_key(pubkey2.encode(), backend=default_backend())

        # Überprüfe die erste Signatur
        public_key1.verify(
            bytes.fromhex(signature1),
            encrypted_contract.encode('utf-8'),
            asym_padding.PSS(mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )

        # Überprüfe die zweite Signatur
        public_key2.verify(
            bytes.fromhex(signature2),
            encrypted_contract.encode('utf-8'),
            asym_padding.PSS(mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )

        print("\n\nSignature verification successful")

    except InvalidSignature:
        print("Verification failed. The signatures do not match the encrypted contract.")

