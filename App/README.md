# Contract Creation and Storage in Ethereum Sepolia Blockchain

## Overview

This document provides a step-by-step guide to creating, signing, encrypting, and storing a contract between two parties in the Ethereum Sepolia Blockchain. The process includes creating a textual contract, generating asymmetric key pairs, and storing the encrypted contract in the blockchain. Follow the instructions below to successfully complete the process.

## Pre-conditions

- **Two Parties Agreement**: Both parties must agree to create a contract.
- **Contract Text File**: The contract must be written in text form and saved in `Example Data/Contract (example.txt)`.
- **Asymmetric Key Pairs**: Both parties must generate an asymmetric key pair (e.g., using [this tool](https://travistidwell.com/jsencrypt/demo/)). Normally, the Public Keys would be contained in X.509 certificates. However, for simplicity in this example, the key pairs are generated using a random generator.
  - Example key pairs in PEM format are provided in the file `Example Data/Keys (example).txt`.
- **Sepolia Wallet**: One party must have a wallet containing Sepolia Ether.
- **Infura API Key**: Create an Infura Ethereum Sepolia API Key [here](https://www.infura.io/?utm_source=google&utm_medium=paidsearch&utm_campaign=Infura-Search-EMEA-en-Brand-PHR&utm_term=infura%20api%20key&gad=1&gclid=CjwKCAjw_uGmBhBREiwAeOfsd0UkKvcyfHxwlUv3cBLiU9YfEGInKOOTjB3kNbFmkmgwQTHmbMCZdxoCZXAQAvD_BwE), and paste it into file `App/WriteBlockchain.py` of this repo in line 53 where the comment `# Paste here your infura API Key!!!` is written.

## Process

1. **Open Terminal**: Navigate to the `App` folder.
2. **Run the Program**: Execute `python3 Application.py` to open the GUI window.
3. **Enter Key Pairs (Party 1)**: The first party enters their key pairs and clicks "Hide" for the private key.
4. **Enter Key Pairs (Party 2)**: The second party does the same.
5. **Provide Wallet Details**: Enter the wallet address and private key of the wallet containing Sepolia Ether.
6. **Select Contract**: Choose "Select Contract" and select `Example Data/Contract (example.txt)`.
7. **Sign & Encrypt Contract**: Click "Sign & Encrypt Contract". A new GUI window will show the Contract-ID, symmetric key, and encrypted contract. (Note: Store the Contract-ID and symmetric key securely.)
8. **Store in Sepolia Blockchain**: Click this button to store the Contract ID, encrypted contract, signatures, and public keys in the blockchain. A confirmation will appear in the terminal within a minute.
9. **Verify Storage**: Visit [Sepolia Etherscan](https://sepolia.etherscan.io/) and search for the smart contract address `0xFF02dA7f654cd106Be934D2DbBEF888c95176724`. View the latest transactions and click "Logs" to see the stored data.
