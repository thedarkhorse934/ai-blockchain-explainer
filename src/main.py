# main.py
# Entry point for AI Transaction Explainer

from ai.ai_explainer import explain_transaction

# Sample transaction data (from Stage 2 output)
sample_tx = {
    "from": "0xYourFromAddress",
    "to": "0xYourToAddress",
    "value": 1000000000000000000,  # 1 ETH in Wei
    "gas": 21000,
    "blockNumber": 1234567,
    "hash": "0x20c4b5ac97f191a7d7e2859766306dd95c60a8d580afdcb6b990b8b5b6723231"
}

def main():
    print("AI Transaction Explainer")
    print("------------------------\n")

    explanation = explain_transaction(sample_tx)
    print(explanation)

if __name__ == "__main__":
    main()
