// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract BusinessContractV2 {
    // Datenstruktur für einen Vertrag
    struct Contract {
        string encryptedContract; // Symmetrisch verschlüsselter Contract
        string pubkey1;
        string pubkey2;
        string signature1; // Signatur 1 angewendet auf verschlüsselten Contract
        string signature2; // Signatur 2 angewendet auf verschlüsselten Contract
    }

    // Mapping von contractId zu Contract
    mapping (string => Contract) private contracts;

    // Event, das geloggt wird, wenn ein Vertrag gespeichert wird
    event ContractStored(string contractId, string encryptedContract, string pubkey1, string pubkey2, string signature1, string signature2);

    // Funktion zum Speichern eines Vertrags
    function storeContract(string memory contractId, string memory encryptedContract, string memory pubkey1, string memory pubkey2, string memory signature1, string memory signature2) public {
        Contract memory newContract = Contract({
            encryptedContract: encryptedContract,
            pubkey1: pubkey1,
            pubkey2: pubkey2,
            signature1: signature1,
            signature2: signature2
        });

        contracts[contractId] = newContract;

        // Loggt das Ereignis
        emit ContractStored(contractId, encryptedContract, pubkey1, pubkey2, signature1, signature2);
    }

    // Funktion zum Abrufen der Daten eines Vertrags anhand der contractId
    function getContract(string memory contractId) public view returns (string memory encryptedContract, string memory pubkey1, string memory pubkey2, string memory signature1, string memory signature2) {
        Contract memory contractData = contracts[contractId];
        return (contractData.encryptedContract, contractData.pubkey1, contractData.pubkey2, contractData.signature1, contractData.signature2);
    }
}
