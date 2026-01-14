import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")

if not RPC_URL:
    raise Exception("RPC_URL not found in environment variables")

w3 = Web3(Web3.HTTPProvider(RPC_URL))


def fetch_transaction(tx_hash: str):
    """
    Fetch a transaction from the Ethereum blockchain using its hash.
    """
    if not w3.is_connected():
        raise Exception("Failed to connect to Ethereum RPC")

    tx = w3.eth.get_transaction(tx_hash)
    return tx
