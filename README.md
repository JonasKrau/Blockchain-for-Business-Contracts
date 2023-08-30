# Blockchain for Business Contracts

## Overview

The **Blockchain for Business Contracts** project aims to optimize the way business contracts are signed and stored by leveraging the power of blockchain technology. Our web application provides a secure, transparent, and decentralized platform for signing and storing business contracts. With the immutability and distributed nature of the blockchain, we ensure the integrity and authenticity of contracts, making them tamper-proof and auditable. This project is developed and tested on Ubuntu, and it requires Python to be installed on your system.

## Key Features

- **Secure Contract Signing**: Users can upload their business contract files and sign them using their private keys, ensuring that only authorized parties can modify the contract.
- **Encrypted and Signed Contract Storage on Blockchain**: The signed and encrypted business contracts, along with the public keys, are securely stored on the blockchain. This provides an authentic, immutable, decentralized, and robust storage solution, eliminating the need for centralized systems and reducing the risk of data tampering or loss. By ensuring the confidentiality and privacy of the contract data, and making it inaccessible to unauthorized parties, this method provides an unparalleled level of transparency and security.
- **Transparency and Auditing**: The blockchain's public and transparent nature allows for easy auditing of contract history. Any changes or updates to the contract are recorded on the blockchain, providing a clear and verifiable audit trail.
- **Decentralized Control**: The use of blockchain technology ensures that no single entity has full control over the contract signing and storage process. This decentralization enhances trust and security.

## Problem Statement

Traditional methods of signing and storing business contracts are plagued with issues like data tampering, lack of transparency, and dependence on centralized authorities. This can lead to disputes, legal challenges, and difficulties in verifying the authenticity of contracts. Additionally, relying on third-party intermediaries for contract storage raises concerns about data privacy and security.

## Our Solution

The **Blockchain for Business Contracts** solution addresses these challenges by harnessing blockchain technology to create a transparent, secure, and decentralized platform for signing and storing business contracts. By utilizing cryptographic signatures and blockchain's distributed ledger, we ensure the integrity and authenticity of each contract. The contracts are stored in a tamper-proof and auditable manner, making them easily verifiable and reducing the risk of disputes.

## Advantages

- **Security**: Blockchain's cryptographic algorithms and decentralized nature ensure that business contract data remains secure and tamper-proof.
- **Transparency**: All activities related to business contracts are recorded on the blockchain, providing a transparent and auditable history of the contracts.
- **Data Integrity**: By using digital signatures, we guarantee that the business contracts remain unchanged throughout their lifecycle.
- **Trustless Verification**: Users can independently verify the authenticity of a business contract without relying on third-party intermediaries.
- **Cost-Efficient**: Eliminating the need for centralized storage and intermediaries reduces operational costs for businesses.
- **Accessibility**: The web-based platform allows users to sign and store business contracts conveniently from anywhere.

## Smart Contract Integration

Within the `SC` folder, you will find the Smart Contract file `Contract.sol`. This Smart Contract contains essential functions for storing and retrieving contract data. However, users utilizing this repository do not need to manually run this Smart Contract. Instead, it is employed by the Python applications to handle the storage and retrieval of contract details, providing seamless integration within the system.

## Installation

To get started with **Blockchain for Business Contracts**, follow these steps:

1. **Install Python**: You'll need to have Python installed on your system.
2. **Clone the Repository**: Download this repository to your local machine.
3. **Install Dependencies**: Inside the repository directory, run the following command to install the required external libraries:
    ```
    pip install -r requirements.txt
    ```
4. **App and Lookup Folders**: Inside the repository, you'll find two main folders: `App` and `Lookup`. Begin by reading the README file inside the `App` folder, as it contains detailed instructions on setting up and running the application. Using the App Folder, contractors can store encrypted and digitally signed contracts on the Ethereum Sepolia Blockchain. Further instructions and information can be found in the README file within the `Lookup` folder. This can then be used to later retrieve the contract data stored in the Ethereum Sepolia Blockchain, verify the signatures, and decrypt the contract. Following these guidelines will ensure a smooth setup and a comprehensive understanding of how to utilize the system.

## License

This project is licensed under the Apache License, Version 2.0. The full text of the license can be found in the [LICENSE](LICENSE) file included in this repository. By using, distributing, or contributing to this project, you agree to abide by the terms and conditions of this license.

## Contact

If you have any questions or would like more information, please feel free to contact me:

- **Name**: Jonas Krause
- **E-Mail**: [krause@tu-berlin.de](mailto:krause@tu-berlin.de)
