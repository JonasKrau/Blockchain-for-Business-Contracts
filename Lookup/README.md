# Lookup Function for Ethereum Sepolia Blockchain

This tool allows you to download a stored encrypted contract with all its details from the Ethereum Sepolia Blockchain. It verifies the digital signatures of the contracting parties, decrypts the contract, and displays it in plain text.

> **Note**: This lookup function should only be performed after the contract has been written to the blockchain, as described in the [README.md file in the App folder](../App/README.md).

## Pre-conditions

- **Infura API Key**: Paste the previously created Infura Ethereum Sepolia API Key (as described in [App/README.md](../App/README.md)) into the file `Lookup/lookup.py` of this repository on line 15 where the comment `# Paste here your infura API Key!!!` is written.

## Process

Follow these steps to retrieve a contract from the Ethereum Sepolia Blockchain:

1. **Open the Terminal**: Open the terminal on your computer.

2. **Navigate to the Folder**: Navigate to the folder containing the `lookup.py` file.

3. **Run the Command**: Execute the following command in the terminal:
    ```bash
    python3 lookup.py
    ```
   A GUI window will open.

4. **Input Contract ID**: Enter the Contract ID of the contract that you received when creating the blockchain entry.

5. **Input Symmetric Key**: Enter the symmetric key that you have securely stored and kept secret.

6. **Get Contract Data**: Click on "Get Contract Data." If you have entered the correct information, the terminal will display the data downloaded from the blockchain, information on whether the signatures were successfully verified, and the decrypted contract in plain text. You will also see the corresponding contract in plain text in another GUI window.
