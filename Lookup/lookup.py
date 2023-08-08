from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/0b9f3b7753854e3482962cf27f6aa40c'))
    
# Contract-Adresse und ABI (Schnittstellenbeschreibung)
contract_address = '0xC5fb728194F843061479ddFDe12106A667052a1e'
contract_address = Web3.to_checksum_address(contract_address)
contract_abi = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "string",
				"name": "contractId",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "encryptedSignature",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "pubkey1",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "pubkey2",
				"type": "string"
			}
		],
		"name": "ContractStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "contractId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "encryptedSignature",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pubkey1",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pubkey2",
				"type": "string"
			}
		],
		"name": "storeContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "contractId",
				"type": "string"
			}
		],
		"name": "getContract",
		"outputs": [
			{
				"internalType": "string",
				"name": "encryptedSignature",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pubkey1",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pubkey2",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]    



def get_contract_transactions():


    from_block = 0

    # Logs abrufen
    logs = web3.eth.get_logs({
        'fromBlock': from_block,
        'address': contract_address
    })

    # Entsprechende Transaktionshashes ausgeben, Liste sortiert nach dem Alter der Transaktionen (beginnend mit der ältesten Transaktion)
    transaction_hashes = [log['transactionHash'].hex() for log in logs]
    
    return transaction_hashes

# Verwendungsbeispiel
transaction_hashes = get_contract_transactions()
print(transaction_hashes)



