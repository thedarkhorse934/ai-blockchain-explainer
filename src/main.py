from blockchain.fetch_transaction import fetch_transaction


def main():
    tx_hash = "0x20c4b5ac97f191a7d7e2859766306dd95c60a8d580afdcb6b990b8b5b6723231"

    tx = fetch_transaction(tx_hash)

    print("Transaction fetched successfully")
    print("------------------------------")
    print(f"From: {tx['from']}")
    print(f"To: {tx['to']}")
    print(f"Value (wei): {tx['value']}")
    print(f"Gas: {tx['gas']}")
    print(f"Block Number: {tx['blockNumber']}")
    print(f"Transaction Hash: {tx['hash'].hex()}")


if __name__ == "__main__":
    main()

