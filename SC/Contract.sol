// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract BusinessContractV2 {
    // Data structure for a contract
    struct Contract {
        string encryptedContract; // Symmetric encrypted contract
        string pubkey1;
        string pubkey2;
        string signature1; // Signature 1 applied to encrypted contract
        string signature2; // Signature 2 applied to encrypted contract
    }

    // Mapping from contractId to contract
    mapping (string => Contract) private contracts;

    // Event that is logged when a contract is saved
    event ContractStored(string contractId, string encryptedContract, string pubkey1, string pubkey2, string signature1, string signature2);

    // Function to save a contract
    function storeContract(string memory contractId, string memory encryptedContract, string memory pubkey1, string memory pubkey2, string memory signature1, string memory signature2) public {
        Contract memory newContract = Contract({
            encryptedContract: encryptedContract,
            pubkey1: pubkey1,
            pubkey2: pubkey2,
            signature1: signature1,
            signature2: signature2
        });

        contracts[contractId] = newContract;

        // Logs the event
        emit ContractStored(contractId, encryptedContract, pubkey1, pubkey2, signature1, signature2);
    }

    // Function to retrieve the data of a contract based on the contractId
    function getContract(string memory contractId) public view returns (string memory encryptedContract, string memory pubkey1, string memory pubkey2, string memory signature1, string memory signature2) {
        Contract memory contractData = contracts[contractId];
        return (contractData.encryptedContract, contractData.pubkey1, contractData.pubkey2, contractData.signature1, contractData.signature2);
    }
}
