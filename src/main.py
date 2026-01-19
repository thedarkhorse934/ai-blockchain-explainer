from blockchain.fetch_transaction import fetch_transaction
from ai.ai_explainer import explain_transaction

USE_LIVE_DATA = False  # change to True when you want real Sepolia data

TX_HASH = "0x20c4b5ac97f191a7d7e2859766306dd95c60a8d580afdcb6b990b8b5b6723231"

sample_tx = {
    "from": "0xYourFromAddress",
    "to": "0xYourToAddress",
    "value": 1000000000000000000,
    "gas": 21000,
    "blockNumber": 1234567,
    "hash": TX_HASH
}

def main():
    if USE_LIVE_DATA:
        print("Using live Sepolia transaction data...\n")
        tx = fetch_transaction(TX_HASH)
    else:
        print("Using sample transaction data...\n")
        tx = sample_tx

    explanation = explain_transaction(tx)
    print(explanation)

if __name__ == "__main__":
    main()
