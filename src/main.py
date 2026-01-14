from blockchain.fetch_transaction import fetch_transaction


def main():
    tx_hash = "PUT_A_SEPOLIA_TX_HASH_HERE"

    tx = fetch_transaction(tx_hash)

    print("Transaction fetched successfully")
    print("------------------------------")
    print(f"From: {tx['from']}")
    print(f"To: {tx['to']}")
    print(f"Value (wei): {tx['value']}")


if __name__ == "__main__":
    main()
