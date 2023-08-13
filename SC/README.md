# BusinessContractV2 Smart Contract

## Overview

`BusinessContractV2` is a Solidity smart contract that has been developed to handle the storage and retrieval of encrypted business contracts. It forms a critical part of the **Blockchain for Business Contracts** system by interacting seamlessly with the associated Python applications. The contract has been optimized for functionality within the Ethereum blockchain.

## Structure

The smart contract consists of:

- **Contract Structure**: Defines the attributes of a contract including the encrypted contract data, public keys of the signing parties, and the respective signatures.
- **Contracts Mapping**: A mapping between contract IDs and the corresponding contract data.
- **ContractStored Event**: Logs when a contract is stored within the system.
- **Store and Retrieve Functions**: Functions for storing and retrieving contract data.

## Functions

### storeContract

The `storeContract` function allows the Python applications to store encrypted and signed contract details. It accepts the following parameters:

- `contractId`: A unique identifier for the contract.
- `encryptedContract`: The symmetrically encrypted contract data.
- `pubkey1`, `pubkey2`: Public keys of the two parties involved.
- `signature1`, `signature2`: Signatures applied to the encrypted contract.

The function then logs the `ContractStored` event.

### getContract

The `getContract` function allows the Python applications to retrieve the details of a contract using its contractId. The Python application can call this function to obtain all related data including the encrypted contract, public keys, and signatures.

## Integration with Python Applications

The Python applications within the **Blockchain for Business Contracts** system utilize the `BusinessContractV2` Smart Contract for storing and retrieving contract details. This integration provides seamless storage and retrieval of contract details:

- **Storing**: The Python application utilizes the `storeContract` function when it needs to save a new business contract, sending all necessary data as arguments.
- **Retrieving**: When it is necessary to fetch a stored contract, the Python application uses the `getContract` function, passing the relevant contractId.

## Monitoring Transactions

All transactions executed by this Smart Contract can be tracked on Sepolia's Etherscan by visiting the following link with the smart contract's address: [0xFF02dA7f654cd106Be934D2DbBEF888c95176724](https://sepolia.etherscan.io/address/0xFF02dA7f654cd106Be934D2DbBEF888c95176724). This provides full transparency over the contract's operations, including the storing and retrieving functions.

## Development

This smart contract is written using Solidity and can be compiled with a compiler version of `>=0.4.22 <0.9.0`. For local development, tools like Truffle can be used, and for deployment, networks like Ethereum can be leveraged.
