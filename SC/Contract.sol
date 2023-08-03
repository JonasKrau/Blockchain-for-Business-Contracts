// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract BusinessContract {
    // Datenstruktur für einen Vertrag
    struct Contract {
        string encryptedSignature;
        string pubkey1;
        string pubkey2;
    }

    // Mapping von contractId zu Contract
    mapping (string => Contract) private contracts;

    // Funktion zum Speichern eines Vertrags
    function storeContract(string memory contractId, string memory encryptedSignature, string memory pubkey1, string memory pubkey2) public {
        Contract memory newContract = Contract({
            encryptedSignature: encryptedSignature,
            pubkey1: pubkey1,
            pubkey2: pubkey2
        });
        
        contracts[contractId] = newContract;
    }
}
