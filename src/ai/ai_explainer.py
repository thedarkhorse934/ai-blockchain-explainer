def explain_transaction(tx):
    value_eth = tx["value"] / 10**18  # convert Wei to ETH
    explanation = (
        f"Transaction {tx['hash']} was sent from {tx['from']} to {tx['to']}.\n"
        f"Amount transferred: {value_eth} ETH\n"
        f"Gas used: {tx['gas']}\n"
        f"Included in block number: {tx['blockNumber']}\n"
    )
    return explanation
