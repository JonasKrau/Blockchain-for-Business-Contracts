// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract BusinessContractV2 {
    // Datenstruktur für einen Vertrag
    struct Contract {
        string encryptedSignature;
        string pubkey1;
        string pubkey2;
    }

    // Mapping von contractId zu Contract
    mapping (string => Contract) private contracts;

    // Event, das geloggt wird, wenn ein Vertrag gespeichert wird
    event ContractStored(string contractId, string encryptedSignature, string pubkey1, string pubkey2);

    // Funktion zum Speichern eines Vertrags
    function storeContract(string memory contractId, string memory encryptedSignature, string memory pubkey1, string memory pubkey2) public {
        Contract memory newContract = Contract({
            encryptedSignature: encryptedSignature,
            pubkey1: pubkey1,
            pubkey2: pubkey2
        });

        contracts[contractId] = newContract;

        // Loggt das Ereignis
        emit ContractStored(contractId, encryptedSignature, pubkey1, pubkey2);
    }

    // Funktion zum Abrufen der Daten eines Vertrags anhand der contractId
    function getContract(string memory contractId) public view returns (string memory encryptedSignature, string memory pubkey1, string memory pubkey2) {
        Contract memory contractData = contracts[contractId];
        return (contractData.encryptedSignature, contractData.pubkey1, contractData.pubkey2);
    }
}
